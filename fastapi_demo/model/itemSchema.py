from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str
    description: str  = Field(None, title='备注', description='项目描述')


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int = Field(None, title='ID', description='项目ID')
    owner_id: int= Field(None, title='用户ID', description='用户ID')

    class Config:
        orm_mode = True
