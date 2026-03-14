from pydantic import BaseModel

class TaskCreate(BaseModel):
    description: str

