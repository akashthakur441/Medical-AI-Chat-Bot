from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.chat_service import generate_response


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    result = generate_response(request.message)

    return {
        "message": request.message,
        "answer": result["answer"],
        "sources": result["sources"],
    }