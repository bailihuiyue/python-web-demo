from sqlalchemy.orm import Session

from fastapi_demo.model import itemSchema
from fastapi_demo.table import models


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: itemSchema.ItemCreate, user_id: int):
    db_item = models.Item(item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
