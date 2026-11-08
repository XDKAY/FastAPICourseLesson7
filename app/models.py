from typing import Annotated
from pydantic import BaseModel, Field, field_validator


class FeedbackRequestScheme(BaseModel):
    username: Annotated[str, Field(min_length=2, max_length=50)]
    message: Annotated[str, Field(min_length=10, max_length=500)]

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        for word in (
            "редиска", "редиске", "редиску", "редиской", "редиски",
            "бяка", "бякой", "бяку", "бяке", "бяки",
            "козявка", "козявкой", "козявке", "козявку", "козявки"
        ):
            if word in value:
                raise ValueError("Использование недопустимых слов")

        return value


class FeedbackResponseScheme(BaseModel):
    message: str
