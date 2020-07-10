# offical-website-backend
 offical-website后端

启动:uvicorn main:app --reload

注意：

uvicorn main:app 命令指:

main: main.py 文件(也可理解为Python模块).
app: main.py 中app = FastAPI()语句创建的app对象.
--reload: 在代码改变后重启服务器，只能在开发的时候使用

Swagger UI: http://127.0.0.1:8000/docs

sql连接库:PyMySQL
orm:SQLAlchemy