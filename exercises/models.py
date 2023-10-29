from pydantic import BaseModel


class ExerciseCreate(BaseModel):
    name: str
    notation: str


class Exercise(ExerciseCreate):
    id: int



