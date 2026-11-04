from datetime import datetime
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: datetime

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)

class ChatResponse(BaseModel):
    answer: str
    received_message: str
    timestamp: datetime

class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=100)
    num_questions: int = Field(default=3, ge=1, le=20)

class QuizQuestion(BaseModel):
    id: int
    question: str
    options: list[str]
    answer: str

class QuizResponse(BaseModel):
    topic: str
    total_questions: int
    questions: list[QuizQuestion]

class SummariseRequest(BaseModel):
    text: str = Field(..., min_length=5, max_length=10000)
    max_bullets: int = Field(default=3, ge=1, le=10)

class SummariseResponse(BaseModel):
    summary: str
    bullets: list[str]
    bullet_count: int
    original_length: int

