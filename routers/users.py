from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas import users
from models import users as models
from dependencies import get_db


router = APIRouter()


@router.post('/users/', response_model=users.User)
def create_user(user:users.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email==user.email).first()
    if db_user:
        raise HTTPException(detail="email already exist", status_code=400)
    user = models.User(email=user.email, username=user.username, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/users/{user_id}', response_model=users.User)
def read_user(user_id:int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id==user_id).first()
    if db_user is None:
        raise HTTPException(detail="user not found", status_code=404)
    return db_user