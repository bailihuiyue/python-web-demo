from typing import List
from pydantic import BaseModel, EmailStr
from pydantic.fields import Field

from fastapi_demo.model.itemSchema import Item


class UserBase(BaseModel):
    email: EmailStr = Field(None, title='邮箱', description='例：ma@qq.com')


class UserCreate(UserBase):
    password: str = Field(None, title='密码', description='用户密码', max_length=20, min_length=6)


class User(UserBase):
    id: int = Field(None, title='用户ID')
    is_active: bool = Field(1, title='激活状态', description='是否激活状态 1 是 0否', alias='isActive')
    items: List[Item] = Field([], title='拥有项目', description='用户名下拥有的项目')

    class Config:
        orm_mode = True
