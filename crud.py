# from sqlalchemy.orm import Session
# import models, schemas

# def create_user(db: Session, user: schemas.UserCreate):
#     new_user = models.User(name=user.name, email=user.email)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user