# from fastapi import FastAPI
# from database import SessionLocal
# from models import Task
# from schemas import TaskCreate
# from database import engine
# from fastapi import FastAPI 
# import models
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# # CREATE TASK
# @app.post("/tasks")
# def create_task(task: TaskCreate):

#     db = SessionLocal()

#     new_task = Task(description=task.description)

#     db.add(new_task)
#     db.commit()

#     return {"message": "Task created"}

# # GET TASKS
# @app.get("/tasks")
# def get_tasks():

#     db = SessionLocal()

#     tasks = db.query(Task).all()

#     return tasks


# # UPDATE TASK
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, task: TaskCreate):

#     db = SessionLocal()

#     existing_task = db.query(Task).filter(Task.id == task_id).first()

#     existing_task.description = task.description

#     db.commit()

#     return {"message": "Task updated"}

# # DELETE TASK
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):

#     db = SessionLocal()

#     task = db.query(Task).filter(Task.id == task_id).first()

#     db.delete(task)

#     db.commit()

#     return {"message": "Task deleted"}



from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, crud
from database import engine, SessionLocal
from schemas import TaskCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.description)


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task.description)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)