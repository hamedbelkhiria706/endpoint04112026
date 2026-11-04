from fastapi import APIRouter
from app.schemas import QuizQuestion, QuizRequest, QuizResponse

router = APIRouter(tags=["Quiz"])

@router.post("/quiz", response_model=QuizResponse)
def post_quiz(payload: QuizRequest):
    questions = [
        QuizQuestion(
            id=index,
            question=f"Sample question {index} about {payload.topic}?",
            options=[
                f"{payload.topic} Answer option 1",
                f"{payload.topic} Answer option 2",
                f"{payload.topic} Answer option 3",
                f"{payload.topic} Answer option 4",
            ],
            answer=f"{payload.topic} Answer option 1",
        )
        for index in range(1, payload.num_questions + 1)
    ]
    return QuizResponse(
        topic=payload.topic,
        total_questions=len(questions),
        questions=questions,
    )

