# 🎧 Transcription Pipeline - Abinaya Rajasekara (Intern - HABB)

A **speech-to-text transcription API** built using **FastAPI**, **Whisper**, and **PyTorch**.  
Upload audio files (`.wav`, `.mp3`) and receive transcribed text in JSON format.

---

## 🚀 Features

- 🎤 Upload audio and get instant transcription
- ⚡ Runs locally with FastAPI
- 🧠 Uses OpenAI Whisper for transcription
- 🚀 Supports GPU acceleration (CUDA)
- 🔗 Integratable into larger pipelines

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

### 1️⃣ Clone Repository
```bash
git clone https://github.com/abinaya-232001/transcription-pipeline-Abinaya-Rajasekara.git
cd transcription-pipeline-Abinaya-Rajasekara
2️⃣ Create & Activate Virtual Environment
powershell
Copy code
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
powershell
Copy code
pip install -r requirements.txt
4️⃣ Run FastAPI Server
powershell
Copy code
uvicorn app:app --reload
Open Swagger UI at 👉 http://127.0.0.1:8000/docs to test the API.

🧩 How It Works
Upload an audio file via /transcribe endpoint.

Whisper processes the audio.

Returns JSON with transcription.

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
3	Whisper not found	ModuleNotFoundError	Install openai-whisper
4	App not starting	uvicorn missing	Install FastAPI & Uvicorn: pip install fastapi uvicorn
5	PowerShell venv issue	Could not activate	Use full path: .venv\Scripts\activate
6	Pip version warning	Version check error	Ignored (non-critical)

💻 How I Ran & Tested
OS: Windows 11

Terminal: PowerShell

Python: 3.12

Virtual Env: .venv

Commands:

powershell
Copy code
.venv\Scripts\activate
pip install -r requirements.txt
python -c "import torch; print(torch.cuda.is_available())"
uvicorn app:app --reload
Upload harvard.wav via Swagger UI to test.

🧾 requirements.txt
nginx
Copy code
fastapi
uvicorn
torch
openai-whisper
jinja2
sympy
typing-extensions
fsspec
🧪 Example API Request (cURL)
bash
Copy code
curl -X POST \
  'http://127.0.0.1:8000/transcribe' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@harvard.wav;type=audio/wav'
📈 Future Improvements
Real-time streaming transcription

Speaker diarization (multi-voice detection)

Multi-language support

Frontend interface for uploads & display

Cloud deployment (AWS/Azure/Streamlit)

🧑‍💻 Author
Abinaya Rajasekara — Intern, HABB
GitHub: abinaya-232001