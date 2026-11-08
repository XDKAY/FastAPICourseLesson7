from fastapi import FastAPI
from .models import (
    FeedbackRequestScheme,
    FeedbackResponseScheme
)

app = FastAPI(
    title="FastAPI Lesson 7"
)


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.post("/feedback", response_model=FeedbackResponseScheme)
async def feedback_handler(feedback: FeedbackRequestScheme):
    return FeedbackResponseScheme(
        message=f"Спасибо, {feedback.username}! Ваш отзыв сохранён."
    )
