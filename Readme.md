# 🩺 Medical AI Chatbot using RAG

## 📌 Overview

This project is a domain-specific Medical AI Chatbot built using Retrieval-Augmented Generation (RAG). The chatbot answers medical-related questions by retrieving relevant information from medical PDF documents stored in a Pinecone vector database and generating responses using the Groq Llama 3.1 model.

---

## 🚀 Features

- Medical Question Answering
- PDF-based Knowledge Retrieval
- Retrieval-Augmented Generation (RAG)
- Pinecone Vector Database
- HuggingFace Sentence Transformer Embeddings
- Groq Llama 3.1 Integration
- Flask Web Interface

---

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Pinecone
- Groq API
- HuggingFace Embeddings
- Sentence Transformers
- HTML
- CSS

---

# 📂 Project Structure

```
Medical-Chat-Bot/
│
├── Data/
├── research/
├── src/
├── static/
├── templates/
├── app.py
├── store_index.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
cd Medical-Chat-Bot
```

---

## Step 2: Create Conda Environment

```bash
conda create -n medibot python=3.12 -y
```

Activate the environment

```bash
conda activate medibot
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Create a .env File

Create a file named `.env`

```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## Step 5: Create Vector Database

```bash
python store_index.py
```

---

## Step 6: Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:8080
```

---

# 💬 Example Questions

- What is diabetes?
- What are the symptoms of hypertension?
- What causes asthma?
- What is anemia?
- How can I prevent heart disease?

---


# 🔮 Future Improvements

- Voice-based interaction
- Chat history
- Multiple PDF support
- Authentication
- Improved guardrails

---

# 👨‍💻 Author

**Akshay VP**

GitHub: https://github.com/Akshay758

LinkedIn: https://www.linkedin.com/in/akshay-vp-636628270

Portfolio: https://akshay758.github.io/Portfolio/
