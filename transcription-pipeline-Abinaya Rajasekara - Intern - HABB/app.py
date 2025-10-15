from fastapi import FastAPI, File, UploadFile
import whisper
from pydub import AudioSegment
import os

# Set the path to your ffmpeg executable
AudioSegment.ffmpeg = r"C:\Users\ASUS\Downloads\ffmpeg-8.0-essentials_build\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

app = FastAPI()
model = whisper.load_model("base")  # you can use "small", "medium", "large" too

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Save the uploaded file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    # Convert to WAV if not already
    audio_ext = os.path.splitext(file_location)[1].lower()
    if audio_ext != ".wav":
        sound = AudioSegment.from_file(file_location)
        wav_file = file_location.rsplit(".", 1)[0] + ".wav"
        sound.export(wav_file, format="wav")
        os.remove(file_location)
        file_location = wav_file

    # Transcribe
    result = model.transcribe(file_location)
    os.remove(file_location)
    return {"text": result["text"]}
