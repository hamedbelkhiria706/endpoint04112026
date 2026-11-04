from datetime import datetime, timezone
from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse

router = APIRouter(tags=["Chat"])

@router.post("/chat", response_model=ChatResponse)
def post_chat(payload: ChatRequest):
    return ChatResponse(
        answer=f"Received: {payload.message}",
        received_message=payload.message,
        timestamp=datetime.now(timezone.utc)
    )

