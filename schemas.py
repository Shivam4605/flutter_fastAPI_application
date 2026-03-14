# from pydantic import BaseModel

# class UserCreate(BaseModel):
#     name: str
#     email: str

from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str