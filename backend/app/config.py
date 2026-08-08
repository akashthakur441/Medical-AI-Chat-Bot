import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Medical AI Chatbot")
APP_ENV = os.getenv("APP_ENV", "development")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")