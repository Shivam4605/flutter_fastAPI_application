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
        from_attributes = True  # Fixed: was orm_mode (Pydantic v1)