# from sqlalchemy.orm import Session
# import models, schemas

# def create_user(db: Session, user: schemas.UserCreate):
#     new_user = models.User(name=user.name, email=user.email)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

from sqlalchemy.orm import Session
from models import Task

def create_task(db: Session, description: str):
    task = Task(description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def update_task(db: Session, task_id: int, description: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.description = description
        db.commit()
    return task


def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()