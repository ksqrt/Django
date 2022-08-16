### 1. 가동방법

서버 (꼭 sudo 권한으로 실행) (server.py)
실행시 꼭 상대경로 에 위치한뒤 사용할것

```
<!-- 리눅스 -->
sudo /bin/python3 server.py

<!-- 윈도우 -->
    python<ver> server.py
ex) python3.10 server.py
```

이후 http://localhost/ 확인

JSON 메시지 생성기 (index.html)

```
<!-- 리눅스 -->
sudo python3 -m http.server PortNUM
sudo python3 -m http.server 81

<!-- 윈도우 -->
python<ver> -m http.server <portNum>
ex)python3.10 -m http.server 81
```

<!--
문서도 한번 읽어보기
스트링도 전송할수 있도록 변경
trig 부분 사양 맞게 수정
서버쪽에서 res 신호 log 남기기
샘플 로그 남기기
리눅스 / 피시 ip 변경후 테스트하기
담주 월요일 까지 마감
-->

이후 http://localhost/81 확인

파일트리 설명

```
server.py = post 를 받으면 data 파일에 저장후 로그를 남기는 서버

index.html = post json 을 커스텀할 수 있는 클라이언트 서버

log.txt = log
```
