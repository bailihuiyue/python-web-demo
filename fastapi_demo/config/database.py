# 导入SQLAlchemy部分
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 为SQLAlchemy创建数据库
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456@localhost/rest_db"
# 创建一个SQLAlchemy“引擎”
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=16,
    pool_pre_ping=True
)
# SessionLocal该类的每个实例将是一个数据库会话。该类本身还不是数据库会话。
# 一旦我们创建了SessionLocal该类的实例，该实例将成为实际的数据库会话。
# 我们SessionLocal将其命名为有别于Session我们从SQLAlchemy导入的名称。
# 稍后我们将使用Session（从SQLAlchemy导入的一种）。
# 要创建SessionLocal类，请使用函数sessionmaker：

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 现在，我们将使用declarative_base()返回类的函数。
# 稍后，我们将从该类继承以创建每个数据库模型或类（ORM模型）：
Base = declarative_base()
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        print('数据连接关闭')
        db.close()