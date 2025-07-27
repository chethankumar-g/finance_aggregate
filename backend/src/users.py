from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models, db_config
import user as user_schema
import auth
import random
import uuid
router = APIRouter()

uid = f'C{uuid.uuid1}'
@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(db_config.get_db)):
    db_user = models.User(name=user.name, password=auth.hash_password(user.password), gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(db_config.get_db)):
    db_user = db.query(models.User).filter(models.User.customer_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=list[user_schema.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(db_config.get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users