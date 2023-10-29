from models import ExerciseCreate, Exercise

exercises_db = []


def create_exercise(exercise: ExerciseCreate):
    exercise_id = len(exercises_db) + 1
    exercise_db = Exercise(id+exercise_id, **exercise.dict())
    exercises_db.append(exercise_db)
    return exercise_db


def get_exercises():
    return exercises_db


def get_exercise(exercise_id: int):
    for exercise in exercises_db:
        if exercise.id == exercise_id:
            return exercise
    return None


