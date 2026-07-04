"""
Transcription Pipeline API — FastAPI + Whisper + pydub
"""

import logging
import os
import uuid
from pathlib import Path
from typing import Optional

import torch
import whisper
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydub import AudioSegment
from starlette.concurrency import run_in_threadpool

# --------------------------------------------------------------------------
# Configuration (override via environment variables, don't hardcode paths)
# --------------------------------------------------------------------------
WHISPER_MODEL_NAME = os.getenv("WHISPER_MODEL", "base")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
FFMPEG_PATH = os.getenv("FFMPEG_PATH")  # optional; only set if ffmpeg isn't on PATH
ALLOWED_EXTENSIONS = {".wav", ".mp3", ".m4a", ".ogg", ".flac"}
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
TEMP_DIR = Path(os.getenv("TEMP_DIR", "temp_audio"))
TEMP_DIR.mkdir(exist_ok=True)

if FFMPEG_PATH:
    AudioSegment.converter = FFMPEG_PATH

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("transcription-pipeline")

app = FastAPI(title="Transcription Pipeline", version="1.0.0")

logger.info(f"Loading Whisper model '{WHISPER_MODEL_NAME}' on device '{DEVICE}'...")
model = whisper.load_model(WHISPER_MODEL_NAME, device=DEVICE)
logger.info("Model loaded.")


@app.get("/health")
async def health():
    return {"status": "ok", "model": WHISPER_MODEL_NAME, "device": DEVICE}


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    original_ext = Path(file.filename or "").suffix.lower()

    if original_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{original_ext}'. Allowed: {sorted(ALLOWED_EXTENSIONS)}",
        )

    job_id = uuid.uuid4().hex
    raw_path = TEMP_DIR / f"{job_id}{original_ext}"
    wav_path: Optional[Path] = None

    try:
        size = 0
        with open(raw_path, "wb") as f:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)
                if size > MAX_FILE_SIZE_BYTES:
                    raise HTTPException(
                        status_code=413,
                        detail=f"File exceeds max size of {MAX_FILE_SIZE_MB} MB",
                    )
                f.write(chunk)

        if original_ext != ".wav":
            wav_path = TEMP_DIR / f"{job_id}.wav"
            try:
                await run_in_threadpool(_convert_to_wav, raw_path, wav_path)
            except Exception as exc:
                logger.exception("Audio conversion failed")
                raise HTTPException(status_code=422, detail="Could not process audio file") from exc
            transcribe_path = wav_path
        else:
            transcribe_path = raw_path

        try:
            result = await run_in_threadpool(model.transcribe, str(transcribe_path))
        except Exception as exc:
            logger.exception("Transcription failed")
            raise HTTPException(status_code=500, detail="Transcription failed") from exc

        return {"text": result["text"], "language": result.get("language")}

    finally:
        for p in (raw_path, wav_path):
            if p and p.exists():
                try:
                    p.unlink()
                except OSError:
                    logger.warning(f"Failed to remove temp file: {p}")


def _convert_to_wav(src: Path, dst: Path) -> None:
    sound = AudioSegment.from_file(src)
    sound.export(dst, format="wav")
