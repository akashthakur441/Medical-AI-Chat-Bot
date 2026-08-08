from fastapi import FastAPI

from backend.app.config import APP_NAME
from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.chat import router as chat_router


app = FastAPI(title=APP_NAME)


app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Medical AI Chatbot API is running",
        "environment": "development"
    }