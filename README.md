# 🎧 Transcription Pipeline - Abinaya Rajasekara (Intern - HABB)

**Speech-to-text API** using **FastAPI**, **Whisper**, and **PyTorch**.  
Upload audio files (`.wav`, `.mp3`) → get **transcribed text** in JSON.

---

## 🚀 Features

- 🎤 Instant transcription from audio  
- ⚡ Runs locally with FastAPI  
- 🧠 Whisper model for high-quality transcription  
- 🚀 GPU acceleration supported (CUDA)  
- 🔗 Easy integration into pipelines or dashboards  

---

## 🛠️ Tools & Technologies

- Python 3.12 | FastAPI | Uvicorn  
- OpenAI Whisper | PyTorch (CUDA 12.1)  
- Jinja2 | Sympy | Typing-Extensions  

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
