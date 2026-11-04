from fastapi import FastAPI
from app.routers import chat, health, quiz, summarise

app = FastAPI(
    title="AI Backend API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(health.router)
app.include_router(chat.router)
app.include_router(quiz.router)
app.include_router(summarise.router)

