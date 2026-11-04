from fastapi import APIRouter
from app.schemas import SummariseRequest, SummariseResponse

router = APIRouter(tags=["Summarise"])

@router.post("/summarise", response_model=SummariseResponse)
def post_summarise(payload: SummariseRequest):
    sentences = [item.strip() for item in payload.text.split(".") if item.strip()]
    if not sentences:
        sentences = [payload.text.strip()]
    bullets = [f"Key point: {sentence}" for sentence in sentences[:payload.max_bullets]]
    summary_text = sentences[0] if sentences else payload.text
    return SummariseResponse(
        summary=f"Summary: {summary_text}",
        bullets=bullets,
        bullet_count=len(bullets),
        original_length=len(payload.text),
    )

