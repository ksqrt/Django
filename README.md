# http server

//클라이언트
JSON
192.168.120.20 to 192.168.120.40:80

[ {direction : "REQ" }, {CommandID : 2}, {Command : "TRIG" }, {TRIGGER_ID : 1} ]

[ {direction : "RES" }, {CommandID : 6}, {Command : "RESP" }, {R_STATUS : true} ]
[ {direction : "RES" }, {CommandID : 6}, {Command : "RESP" }, {R_STATUS : false, R_DESCRIPTION: "장비가 이미 시작상태입니다."} ]

//서버
메시지를 수신했습니다.
REQ
2
TRIG
TRIGGER_ID : 1
