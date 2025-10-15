# 🎧 Transcription Pipeline - Abinaya Rajasekara (Intern - HABB) 
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white) 
![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0-green?logo=fastapi&logoColor=white) 
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

```bash
# Clone repository
git clone https://github.com/abinaya-232001/transcription-pipeline-Abinaya-Rajasekara.git
cd transcription-pipeline-Abinaya-Rajasekara

# Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app:app --reload

# Open Swagger UI to test API
# Visit: http://127.0.0.1:8000/docs
🧩 How It Works
Upload an audio file via the /transcribe endpoint.

Whisper processes the audio.

Returns a JSON response containing the transcription.

Example Input: harvard.wav
Example Output:

json
Copy code
{
  "text": "The stale smell of old beer lingers..."
}
📁 Folder Structure
bash
Copy code
transcription-pipeline/
├── app.py                  # FastAPI main application
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── .gitignore              # Ignored files (venv, cache, etc.)
└── audio_files/ (optional) # Folder for test audio files
🧠 Errors Faced & Fixes
Step	Issue	Cause	Solution
1	Torch not using GPU	CUDA unavailable	Install GPU version: pip install torch --index-url https://download.pytorch.org/whl/cu121
2	Dependency conflict	sympy version mismatch	Install compatible version: sympy==1.13.1
3	Whisper not found	ModuleNotFoundError	Install: pip install openai-whisper
4	App not starting	uvicorn missing	Install FastAPI & Uvicorn: pip install fastapi uvicorn
5	PowerShell venv issue	Could not activate	Use full path: .venv\Scripts\activate
6	Pip version warning	Version check error	Ignored (non-critical)

📈 Future Improvements
Real-time streaming transcription

Speaker diarization (multi-voice detection)

Multi-language transcription support

Frontend interface for uploads & display

Cloud deployment (AWS / Azure / Streamlit)

🧑‍💻 Author
Abinaya Rajasekara — Intern, HABB
GitHub: abinaya-232001

✅ Conclusion
This project provides a robust and easy-to-use speech-to-text API. With FastAPI and Whisper integration, it supports GPU acceleration for efficient transcription and can be easily extended or deployed in pipelines, dashboards, or cloud environments.
