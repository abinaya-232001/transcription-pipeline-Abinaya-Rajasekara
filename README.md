# 🎧 Transcription Pipeline - Abinaya Rajasekara (Intern - HABB)  
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white) 
![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0-green?logo=fastapi&logoColor=white) 
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.22.0-purple?logo=uvicorn&logoColor=white) 
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-red?logo=pytorch&logoColor=white) 
![Whisper](https://img.shields.io/badge/Whisper-1.0-orange?logo=openai&logoColor=white) 
![License](https://img.shields.io/badge/License-MIT-blue)

**Speech-to-text API** using **FastAPI**, **Whisper**, and **PyTorch**.  
Upload audio files (`.wav`, `.mp3`) → get **transcribed text** in JSON format.

---

<p align="center">
  <img src="audio_gif.webp" width="600" alt="Audio transcription animation"/>
</p>

## 🚀 Features

- 🎤 Instant transcription from audio  
- ⚡ Runs locally with FastAPI  
- 🧠 Whisper model for high-quality transcription  
- 🚀 GPU acceleration supported (CUDA)  
- 🔗 Easy integration into pipelines or dashboards  

---

## 🛠️ Tools & Technologies

- **Python 3.12**  
- **FastAPI**  
- **Uvicorn**  
- **OpenAI Whisper**  
- **PyTorch (CUDA 12.1)**  
- **Jinja2, Sympy, Typing-Extensions**  

---

## ⚙️ Setup Instructions

1. Clone the repository and navigate to it.  
2. Create and activate a Python virtual environment.  
3. Install dependencies from `requirements.txt`.  
4. Run the FastAPI server.  
5. Open Swagger UI to test the API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).  

---

## 🧩 How It Works

- Upload an audio file via the `/transcribe` endpoint.  
- Whisper processes the audio.  
- Returns a JSON response containing the transcription.

**Example Input:** `harvard.wav`  
**Example Output:**
```json
{
  "text": "The stale smell of old beer lingers..."
}
