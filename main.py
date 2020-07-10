import time

from fastapi import Depends, FastAPI, Header, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from fastapi_demo.api_1 import userApi, itemApi

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# app.mount("/static", StaticFiles(directory="app/static"), name="static") # 挂载静态文件，指定目录
# templates = Jinja2Templates(directory="templates") # 模板目录
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(response.headers)
    return response


app.include_router(userApi.router)
app.include_router(
    itemApi.router,
    prefix="/api",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
origins = [
    "http://localhost.wisdomx.net",
    "http://localhost",
    "http://localhost:8080",
]
# 解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
