# http server

### 1. 필수 라이브러리 설치

방법
pip install requirements.txt

이후 서버열기
uvicorn server:app --reload --port=80
uvicorn server:app --reload --host 100.100.100.1 --port=80

uvicorn server:app --reload --host 111.111.1.78 --port=80

--port=80
uvicorn server:app --reload --host 100.100.100.1 --port=80
