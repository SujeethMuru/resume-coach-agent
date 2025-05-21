# 🧠 Resume Coach Agent

An AI-powered resume feedback tool built with Flask and Ollama, running entirely offline.

## 🚀 Features

- 🔍 Upload your PDF resume for analysis
- 🧠 Get AI-generated feedback using local LLMs (`gemma:2b`)
- 📄 Accepts optional job descriptions to tailor suggestions
- 🗃 Runs locally, requires no OpenAI keys or internet

## 🗂 Project Structure
```
resume-coach-agent/
├── backend/
│ ├── app.py # Flask entrypoint
│ ├── routes/resume.py # API logic
│ ├── services/ # AI logic
│ │ ├── coach.py
│ │ └── ollama_wrapper.py
│ ├── utils/resume_parser.py # PDF parsing
│ └── requirements.txt
├── data/ # Sample resumes
├── models/ # Prompt templates
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the repo

```
bash
git clone https://github.com/your-username/resume-coach-agent.git
cd resume-coach-agent
```

### 2. Create a virtual environment

python -m venv venv
venv\Scripts\activate  # On Windows

### 3. Install dependencies

pip install -r backend/requirements.txt

### 4. Run Ollama

ollama pull gemma:2b
ollama run gemma:2b

### 5. Start Flask backend

cd backend
python app.py

### 6. Test via Postman or curl

Send a POST request to:
http://localhost:5000/api/feedback

With either:

- A PDF file (resume) and optional text field (job)
- Or JSON: { "resume": "...", "job": "..." }

📌 Example Response:
{
  "feedback": "Your resume is clear and well-structured. Use more action verbs..."
}

📜 License
This project is licensed under the MIT License.

### Made with ❤️ by [Sujeeth](https://github.com/SujeethMuru)
