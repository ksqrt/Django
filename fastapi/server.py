import time
import os
import json
# fast api 와 uricorn 을 설치해주는 부분
try:
    import uvicorn
    from fastapi import FastAPI, Request
    from fastapi.middleware.cors import CORSMiddleware
except ModuleNotFoundError as e:
    print(e)
    os.system("pip install fastapi")
    os.system("pip install uvicorn[standard]")


#  Import A module from my own project that has the routes defined
# from redorg.routers import saved_items

origins = [
    'http://localhost:8080',
]


webapp = FastAPI()
# webapp.include_router(saved_items.router)
# 교차출처 리소스 공유
webapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],

)

# -----------------------------------


@webapp.get("/")
def read_root():
    logfile = "fastapi/log.txt"
    with open(logfile, 'r', encoding='utf-8') as log:
        return log.read()


@webapp.post("/")
async def create_item(req: Request):
    # 리퀘스트 바디데이터 정의
    bodydata = await req.json()
    # ---------------------로그남기기-----------------
    log_path = "fastapi/log.txt"

    with open(log_path, 'a', encoding='utf-8') as log:
        log.write(str(bodydata) + "\n")
        log.close()
    # ----------------------데이터저장하기-------------

    filename = "sample"
    file_ext = ".json"
    file_path = "fastapi/data/%s%s" % (filename, file_ext)
    uniq = 1
    output_path = 'fastapi/data/%s%s' % (filename, file_ext)
    # 동일한 값 존재시 +1
    while os.path.exists(output_path):
        # 파일명(1) 파일명(2)...
        output_path = 'fastapi/data/%s(%d)%s' % (filename, uniq, file_ext)
        uniq += 1

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(bodydata, file, indent="\t")

        # ----------------------------RES 리턴
    return bodydata


#!!!! 맨마지막에 배치할것!!!!
def serve():
    """Serve the web application."""
    uvicorn.run(webapp)


if __name__ == "__main__":
    serve()
