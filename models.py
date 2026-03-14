# from sqlalchemy import Column, Integer, Text
# from database import Base

# class Task(Base):

#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(Text)
    
from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255))