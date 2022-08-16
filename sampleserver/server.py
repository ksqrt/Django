from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import os
from datetime import datetime
import json


class myHandler(BaseHTTPRequestHandler):

    # GET형식의 파라미터를 파싱한다.(url의 물음표(?) 이후의 값을 딕셔너리로 파싱한다.
    def __get_Parameter(self, key):
        # 해당 클래스에 __param변수가 선언되었는지 확인한다.
        if hasattr(self, "_myHandler__param") == False:
            if "?" in self.path:
                # url의 ?이후의 값을 파싱한다.
                self.__param = dict(urlparse.parse_qsl(
                    self.path.split("?")[1], True))
            else:
                # url의 ?가 없으면 빈 딕셔너리를 넣는다.
                self.__param = {}
        if key in self.__param:
            return self.__param[key]
        return None
    # POST형식의 form 데이터를 파싱한다.

    def __get_Post_Parameter(self, key):
        # 해당 클래스에 __post_param변수가 선언되었는지 확인한다.
        if hasattr(self, "_myHandler__post_param") == False:
            # 해더로 부터 formdata를 가져온다.
            data = self.rfile.read(int(self.headers['Content-Length']))

            print(data)  # 변수에 담고 바이너리를 dict 타입으로 변환
            # print(type(data))
            dataline = data.decode("utf-8")
            db = json.loads(data)
            # 시간 / 파일이름 저장 output
            # ----------------------데이터저장하기-------------

            # ------------------요청 로그남기기-----------------
            log_path = "./log.txt"
            with open(log_path, 'a', encoding='utf-8') as log:
                now = datetime.now()
                nowdate = str(now.year)+"/" + str(now.month)+"/" + str(now.day) + \
                    "/" + str(now.hour)+":" + str(now.minute) + \
                    ":" + str(now.second) + "  "
                log.write(nowdate+"  "+str(dataline) + "\n")
                log.close()

            if data is not None:
                self.__post_param = dict(urlparse.parse_qs(data.decode()))
            else:
                self.__post_param = {}

             # --------------------응답 로그남기기-----------------
            resJSON = "{\"Direction\": \"RES\", \"Command\": \"RESP\", \"STATUS\" : \"True\", \"DESCRIPTION\" : \"NULL\"}"
            log_path = "./reslog.txt"
            with open(log_path, 'a+', encoding='utf-8') as log:
                now = datetime.now()
                nowdate = str(now.year)+"/" + str(now.month)+"/" + str(now.day) + \
                    "/" + str(now.hour)+":" + str(now.minute) + \
                    ":" + str(now.second) + "  "
                log.write(nowdate+"  "+resJSON + "\n")
                log.close()

        # resFail ="{\"Direction\": \"RES\", \"Command\": \"RESP\", \"STATUS\" : \"False\", \"DESCRIPTION\" : \"\"}"
        if key in self.__post_param:
            return self.__post_param[key][0]

        return resJSON

    # http 프로토콜의 header 내용을 넣는다.
    def __set_Header(self, code):
        # 응답 코드를 파라미터로 받아 응답한다.
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # http 프로토콜의 body내용을 넣는다.
    def __set_Body(self, data):
        # body 응답은 byte형식으로 넣어야 한다.(필요에 의해 주석 해제)
        # response = io.BytesIO()
        # response.write(b"<html><body><form method='post'><input type='text' name='test' value='hello'><input type='submit'></form></body></html>");
        # self.wfile.write(response.getvalue());
        # data(string)를 byte형식으로 변환해서 응답한다.
        self.wfile.write(data.encode())

    # POST 형식의 request일 때 호출된다.
    def do_GET(self):
        # GET 방식의 파라미터의 data 값을 취득한다.
        data = self.__get_Parameter('data')
        # response(응답)할 body내용이다.
        txt = open('log.txt', "r", encoding='utf-8')
        text = txt.read()
        body = text
        # response header code는 200(정상)으로 응답한다.
        self.__set_Header(200)
        # response body는 위 html 코드 내용을 넣는다.
        self.__set_Body(body)
    # POST 형식의 request일 때 호출된다.

    def do_POST(self):
        # response header code는 200(정상)으로 응답한다.
        self.__set_Header(200)
        # resJSON ="{\"Direction\": \"RES\", \"Command\": \"RESP\", \"STATUS\" : \"True\", \"DESCRIPTION\" : \"NULL\" }"
        # response body는 form으로 받은 test의 값으로 응답한다.
        self.__set_Body(self.__get_Post_Parameter('test'))


# http server를 생성한다.
httpd = HTTPServer(('', 80), myHandler)
print("Server is Running.......")
# 서버 중지(Ctrl + Break)가 나올때까지 message 루프를 돌린다.
httpd.serve_forever()
