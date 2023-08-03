from database import Base
from sqlalchemy import Column, String, Integer

# models.Base.metadata.create_all(bind=engine)
# use this code in main.py
# when we did not use alembic(migrations)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username= Column(String)
    password = Column(String)
