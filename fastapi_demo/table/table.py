from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, schema, Index
from sqlalchemy.orm import relationship

from fastapi_demo.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(250), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")


class Menu(Base):
    __tablename__ = 'sys_menu'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True, comment='标题')
    description = Column(String(250), comment='备注')
    code = Column(String(100), comment='编码')
    url = Column(String(150), comment='页面url')
    parent_id = Column(Integer, comment='父菜单id')
    __table_args__ = ({'comment': '系统菜单表'})  # 添加索引和表注释

    # __table_args__ = (Index('index(zone,status)', 'resource_zone', 'resource_status'), {'comment': '系统菜单表'})  #
    # 添加索引和表注释


