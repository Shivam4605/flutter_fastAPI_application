# from pydantic import BaseModel

# class TaskCreate(BaseModel):
#     description: str


from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str

class TaskResponse(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True