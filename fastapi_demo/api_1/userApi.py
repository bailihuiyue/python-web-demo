from typing import List

from fastapi import Depends, HTTPException, APIRouter, Query, Path
from sqlalchemy.orm import Session

from fastapi_demo.config.database import engine, get_db
from fastapi_demo.table import models
from fastapi_demo.model import userSchema, itemSchema
from fastapi_demo.dao import userDao, itemDao

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/users/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userDao.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userDao.create_user(db=db, user=user)


@router.get("/users/", response_model=List[userSchema.User])
def read_users(skip: int = Query(1, description='跳过'), limit: int = Query(100, description='每页记录数'),
               db: Session = Depends(get_db)):
    users = userDao.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=userSchema.User)
def read_user(user_id: int = Path(..., title='用户ID', description='用户ID'), db: Session = Depends(get_db)):
    db_user = userDao.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=itemSchema.Item)
def create_item_for_user(
        user_id: int, item: itemSchema.ItemCreate, db: Session = Depends(get_db)
):
    return itemDao.create_user_item(db=db, item=item, user_id=user_id)
