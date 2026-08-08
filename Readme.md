# 🩺 Medical AI Chatbot using RAG

## 📌 Overview

This project is a domain-focused Medical AI Chatbot designed to provide general medical information using Large Language Models and Retrieval-Augmented Generation (RAG).

The application is being built with a modular FastAPI backend, Groq LLM integration, and a medical document processing pipeline. Medical PDF documents will be processed and used as the knowledge source for generating more grounded and context-aware responses.

---

## 🚀 Features

- Medical Question Answering
- Groq LLM Integration
- FastAPI Backend
- REST API Architecture
- Medical PDF Text Extraction
- Retrieval-Augmented Generation (RAG)
- Medical Document Knowledge Base
- Environment-based Configuration
- Interactive Swagger API Documentation
- Medical Safety-focused Responses

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Groq API
- Llama LLM
- PyPDF
- python-dotenv
- RAG
- Vector Database
- React *(planned)*

---

# 📂 Project Structure

```text
Medical-AI-Chat-Bot/
│
├── backend/
│   └── app/
│       ├── api/
│       │   └── routes/
│       │       ├── health.py
│       │       └── chat.py
│       │
│       ├── services/
│       │   ├── chat_service.py
│       │   ├── llm_service.py
│       │   └── document_service.py
│       │
│       ├── config.py
│       └── main.py
│
├── data/
│   └── documents/
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env

---



## ⚙️ Installation

## Step 1: Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd Medical-AI-Chat-Bot
```

---

## Step 2: Create Virtual Environment
```bash
python -m venv .venv

Activate the environment on Windows:
```bash
.venv\Scripts\activate
---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Create a .env File

Create a file named `.env`

```env
APP_NAME=Medical AI Chatbot
APP_ENV=development
GROQ_API_KEY=your_groq_api_key
```

---

## Step 5: Add Medical Documents

Place medical PDF documents inside:

data/documents/

These documents will be used as the knowledge source for the RAG pipeline.

---

## Step 6: Run the Application

```bash
uvicorn backend.app.main:app --reload
```

Open the API:

http://127.0.0.1:8000

Interactive API documentation:
```
http://127.0.0.1:8000/docs

```

---

# 💬 Example Questions

- What is diabetes?
- What are the symptoms of hypertension?
- What causes asthma?
- What is anemia?
- What are the risk factors for heart disease?

---


# 🔮 Future Improvements

- Retrieval-Augmented Generation (RAG) pipeline
- Text chunking and embeddings
- Vector database integration
- Source-based responses
- Chat history
- Medical safety guardrails
- Prompt injection protection
- Modern React interface
- Authentication

---

# 👨‍💻 Author

**Akash Thakur**

GitHub: https://github.com/akashthakur441

LinkedIn: https://www.linkedin.com/in/akashthakurr/

Portfolio: https://akashthakur441.github.io/Portfolio/
