from exercises.models import Exercise, ExerciseCreate
from exercises.crud import create_exercise, get_exercises, get_exercise
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/exercises", response_model=Exercise)
def create_new_exercise(exercise: ExerciseCreate):
    return create_exercise(exercise)


@app.get("/exercises/")
def read_exercises():
    return get_exercises()


@app.get("/exercises/(exercise_id)")
def read_exercise(exercise_id: int):
    exercise = get_exercise(exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise does not exits")
    return exercise
