# from fastapi import FastAPI
# from database import engine, SessionLocal, Base
# import models
# import schemas

# app = FastAPI()

# Base.metadata.create_all(bind=engine)

# @app.post("/create_user")
# def create_user(user: schemas.UserCreate):

#     db = SessionLocal()

#     new_user = models.User(
#         name=user.name,
#         email=user.email
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return {
#         "message": "User saved successfully",
#         "name": user.name,
#         "email": user.email
#     }


# @app.get("/get_users")
# def get_users():

#     db = SessionLocal()

#     users = db.query(models.User).all()

#     result = []

#     for user in users:
#         result.append({
#             "id": user.id,
#             "name": user.name,
#             "email": user.email
#         })

#     return result



from fastapi import FastAPI
from database import SessionLocal
from models import Task
from schemas import TaskCreate

app = FastAPI()


# CREATE TASK
@app.post("/tasks")
def create_task(task: TaskCreate):

    db = SessionLocal()

    new_task = Task(description=task.description)

    db.add(new_task)
    db.commit()

    return {"message": "Task created"}

# GET TASKS
@app.get("/tasks")
def get_tasks():

    db = SessionLocal()

    tasks = db.query(Task).all()

    return tasks


# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):

    db = SessionLocal()

    existing_task = db.query(Task).filter(Task.id == task_id).first()

    existing_task.description = task.description

    db.commit()

    return {"message": "Task updated"}

# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    db.delete(task)

    db.commit()

    return {"message": "Task deleted"}