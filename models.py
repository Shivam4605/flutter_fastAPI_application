# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):

#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     email = Column(String(100))


from sqlalchemy import Column, Integer, Text
from database import Base

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)