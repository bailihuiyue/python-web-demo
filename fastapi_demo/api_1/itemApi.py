from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi_demo.config.database import engine, get_db
from fastapi_demo.table import models
from fastapi_demo.model import itemSchema
from fastapi_demo.dao import itemDao
from fastapi import APIRouter

router = APIRouter()
models.Base.metadata.create_all(bind=engine)


@router.get("/items/", response_model=List[itemSchema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = itemDao.get_items(db, skip=skip, limit=limit)
    return items
