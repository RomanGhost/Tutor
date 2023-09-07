from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: int = Field(default=None)
    telegram_id: int = Field(default=None)
    login: str = Field(default=None, min_length=3, max_length=25)
    password: str = Field(default=None, max_length=256)
    first_name: str = Field(default=None, min_length=2, max_length=255)
    last_name: str = Field(default=None, min_length=2, max_length=255)
    description: str = Field(default=None, min_length=2, max_length=500)
    phone: str = Field(default=None, min_length=11, max_length=15)
    learning_rate: int = Field(default=None)
    birthday: datetime = Field(default=None)


class Teacher(BaseModel):
    id: int
    user_id: int
    graduation: int
    rating: float
    count_lesson: float


class Lesson(BaseModel):
    id: int
    teacher_id: int
    name: str = Field(min_length=3, max_length=500)
    description: str = Field(min_length=2, max_length=500)
    date_time: datetime
    place: str = Field(min_length=2, max_length=1000)
    age_limit: int = Field(min_items=0, max_items=100)


class Application(BaseModel):
    id: int
    user_id: int
    teacher_id: int
    name: str = Field(min_length=2, max_length=255)
    description: str = Field(min_length=2, max_length=500)


class RateLesson(BaseModel):
    user_id: int
    lesson_id: int
    rate: float
    review: str = Field(min_length=2, max_length=255)
