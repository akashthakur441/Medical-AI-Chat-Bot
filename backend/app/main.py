from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.app.api.routes.chat import router as chat_router


app = FastAPI(
    title="Medical AI Chatbot"
)


app.mount(
    "/static",
    StaticFiles(directory="frontend"),
    name="static",
)


app.include_router(chat_router)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")