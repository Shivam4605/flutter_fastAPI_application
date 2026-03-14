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



from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schemas import TaskCreate, TaskResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency - proper DB session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE TASK
@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"message": "Task created"}


# GET TASKS
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    existing_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    existing_task.description = task.description
    db.commit()
    return {"message": "Task updated"}


# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}