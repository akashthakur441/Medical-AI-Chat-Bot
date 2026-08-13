# 🩺 Medical AI Chatbot using RAG

A domain-focused Medical AI Chatbot built using **Retrieval-Augmented Generation (RAG)** to provide grounded, general medical information from a curated medical knowledge base.

The application combines **FastAPI, Groq LLMs, Sentence Transformers, FAISS, and medical PDF documents** to retrieve relevant medical context before generating a response.

> ⚠️ This application is intended for general educational information only and is not a substitute for professional medical advice, diagnosis, or treatment.

---

## 📌 Overview

The Medical AI Chatbot follows a Retrieval-Augmented Generation architecture.

Instead of sending every medical question directly to the LLM, the application first searches a locally built FAISS vector store for relevant information from medical documents.

The retrieved context is then provided to the Groq-hosted Llama model, which generates the final response.

### 🔄 RAG Pipeline

```text
User Question
      ↓
FastAPI Chat API
      ↓
Query Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Medical Chunks
      ↓
Context + User Question
      ↓
Groq Llama LLM
      ↓
Medical Response
      ↓
Frontend Chat UI


##🚀 Features

🩺 Medical question answering
💬 Natural conversational interaction
🤖 Groq LLM integration
🧠 Llama 3.3 70B model
📚 Retrieval-Augmented Generation (RAG)
📄 Medical PDF document processing
✂️ Text extraction and chunking
🔢 Sentence Transformer embeddings
🔎 FAISS similarity search
📌 Metadata-based document/page tracking
🛡️ Medical safety-focused system instructions
🚫 Reduced hallucination through context-grounded responses
🌐 FastAPI REST API
📖 Interactive Swagger API documentation
💻 Lightweight browser-based chat interface
⚙️ Environment-based API configuration

---

## 🛠️ Tech Stack

Backend
-Python
-FastAPI
-Uvicorn
-Pydantic

LLM
-Groq API
-Llama 3.3 70B Versatile

RAG / NLP
-Sentence Transformers
-all-MiniLM-L6-v2
-FAISS
-NumPy

Document Processing
-PyPDF
-PDF text extraction
-Custom text chunking

Frontend
-HTML
-CSS
-JavaScript

Configuration
-python-dotenv
-Environment variables

---

# 📂 Project Structure

```text
Medical-AI-Chat-Bot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── chat.py
│   │   │   │   └── health.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── services/
│   │   │   ├── chat_service.py
│   │   │   ├── chunking_service.py
│   │   │   ├── document_service.py
│   │   │   ├── embedding_service.py
│   │   │   ├── llm_service.py
│   │   │   ├── retrieval_service.py
│   │   │   └── vector_store.py
│   │   │
│   │   ├── config.py
│   │   └── main.py
│   │
│   └── __init__.py
│
├── data/
│   ├── documents/
│   │   ├── asthma.pdf
│   │   ├── diabetes.pdf
│   │   ├── hypertension.pdf
│   │   └── medical_knowledge_base.pdf
│   │
│   └── vector_store/
│       ├── medical.index
│       └── metadata.json
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── scripts/
│   ├── build_vector_store.py
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_metadata.py
│   ├── test_retrieval.py
│   └── test_similarity.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env


## ⚙️ Installation
---
## Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd Medical-AI-Chat-Bot
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:
```bash
.venv\Scripts\activate
```
---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
---

## Step 4: Create a `.env` File

Create a file named `.env` in the project root:

```env
APP_NAME=Medical AI Chatbot
APP_ENV=development
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

> ⚠️ Never commit your `.env` file or expose your API key publicly.


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

- Voice-based interaction
- Chat history
- Multiple PDF support
- Authentication
- Improved guardrails

---

# 👨‍💻 Author

**Akash Thakur**

GitHub: https://github.com/akashthakur441

LinkedIn: https://www.linkedin.com/in/akashthakurr/

Portfolio: https://akashthakur441.github.io/Portfolio/
