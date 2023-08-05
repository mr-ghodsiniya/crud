from database import Base
from sqlalchemy import Column, String, Integer, Boolean


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
