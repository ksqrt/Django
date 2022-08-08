from datetime import datetime
import os
import json
# fast api 와 uricorn 을 설치해주는 부분
try:
    import uvicorn
    from fastapi import FastAPI, Request
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import HTMLResponse

except ModuleNotFoundError as e:
    print(e)
    os.system("pip install fastapi")
    os.system("pip install uvicorn[standard]")

origins = [
    'http://localhost:8000',
    "*"

]
app = FastAPI()
# app.include_router(saved_items.router)
# 교차출처 리소스 공유
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],

)


def generate_html_response(val):
    html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  </head>
  <body>
    <script>
      function readTextFile() {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET","""+"\""+val+"\""""", true);
        rawFile.onreadystatechange = function () {
          if (rawFile.readyState === 4) {
            var allText = rawFile.responseText;
            document.getElementById("Response").innerHTML = allText;
          }
        };
        rawFile.send();
      }
      $(document).ready(function () {
        readTextFile();
      });
    </script>
    <pre id="Response"></pre>
  </body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def generate_html_response2(val):
    html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  </head>
  <body>
    <script>
      function readTextFile() {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET","""+"\""+val+"\""""", true);
        rawFile.onreadystatechange = function () {
          if (rawFile.readyState === 4) {
            var allText = rawFile.responseText;
            document.getElementById("Response").innerHTML = allText;
          }
        };
        rawFile.send();
      }
      $(document).ready(function () {
        readTextFile();
      });
    </script>
    <pre id="Response"></pre>
  </body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)


def generate_html_response2(val):
    html_content = """
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <script>
      function SetCommand() {
        var cmdid = document.getElementById("CommandId").value;
        var cmdform = document.getElementById("Command");
        var value = "";

        if (cmdid == 1) {
          value = "CHECK";
        } else if (cmdid == 2) {
          value = "TRIGGER";
        } else if (cmdid == 3) {
          value = "LOG";
        } else if (cmdid == 4) {
          value = "CONFIG";
        } else if (cmdid == 5) {
          value = "FUNC";
        } else if (cmdid == 6) {
          value = "RESP";
        }

        cmdform.value = value;

        SetDataSelectBox(cmdid);
      }

      function SetDataSelectBox(cmdid) {
        var DataDiv = document.getElementById("DATADIV");
        if (cmdid == 1) {
          DataDiv.innerHTML =
            "<input type='text' name='CONTENTS' placeholder='CONTENTS'><br />";
        } else if (cmdid == 2) {
          DataDiv.innerHTML =
            "<input type='text' name='ACTION' placeholder='ACTION'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='TPID' placeholder='TPID'><br />";
        } else if (cmdid == 3) {
          DataDiv.innerHTML =
            "<input type='text' name='CAT' placeholder='CAT'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='SEQUENCE' placeholder='SEQUENCE'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='FROM' placeholder='FROM'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='TO' placeholder='TO'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='MEDIUM' placeholder='MEDIUM'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='CONTENTS' placeholder='CONTENTS'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='DESCRIPTION' placeholder='DESCRIPTION'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='COMP_DATA' placeholder='COMP_DATA'><br />";
        } else if (cmdid == 4) {
          DataDiv.innerHTML =
            "<input type='text' name='METHOD' placeholder='METHOD'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='PARAMETERS' placeholder='PARAMETERS'><br />";
        } else if (cmdid == 5) {
          DataDiv.innerHTML =
            "<input type='text' name='TYPE' placeholder='TYPE'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='COMMAND' placeholder='COMMAND'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='DESCRIPTION' placeholder='DESCRIPTION'><br />";
        } else if (cmdid == 6) {
          DataDiv.innerHTML =
            "<input type='text' name='STATUS' placeholder='STATUS'><br />";
          DataDiv.innerHTML +=
            "<input type='text' name='DESCRIPTION' placeholder='DESCRIPTION'><br />";
        }

        //document.form.json.value = JSON.stringify(login);
      }

      function CheckForm() {
        thisform = document.getElementById("SendForm");
        if (thisform.Direction.value == "") {
          thisform.Direction.focus();
        } else if (
          thisform.CommandId.value == "선택하세요" ||
          thisform.CommandId.value == ""
        ) {
          thisform.CommandId.focus();
        } else if (thisform.Command.value == "") {
          thisform.Command.focus();
        } else {
          thisform.submit();
        }
      }
      function CheckFormRes() {
        var formSerializeArray = $("#SendForm").serializeArray();
        var object = {};
        for (var i = 0; i < formSerializeArray.length; i++) {
          object[formSerializeArray[i]["name"]] =
            formSerializeArray[i]["value"];
        }
        var jsonString = JSON.stringify(object);
        //var queryString = $("#SendForm").serialize();
        //var jsonString = JSON.stringify(queryString);
        $.ajax({
          type: "POST",
          url : """+"\""+val+"\""""",
          data: jsonString,
          dataType: "text",
          success: function (result) {
            console.log("ok");
            $("log").html(Response);
            readTextFile();
          },
          error: function (xhr, status, error) {
            console.log("error");
            $("log").html(error);
            readTextFile();
          },
        });
      }

      function readTextFile() {
        var rawFile = new XMLHttpRequest();
        rawFile.open("GET", "log.txt", true);
        rawFile.onreadystatechange = function () {
          if (rawFile.readyState === 4) {
            var allText = rawFile.responseText;
            document.getElementById("Response").innerHTML = allText;
          }
        };
        rawFile.send();
      }
      $(document).ready(function () {
        readTextFile();
      });
    </script>
  </head>
  <body>
    <!-- <br /><br /><br /> -->
    <!-- 
    1. 서버 시간 로그저장 서버로 접속시 저장된 로그 출력<br />
    2. 서버 가동방법 <br />
    Receive : sudo python3 server.py<br />
    Send : sudo python3 -m http.server PortNUM<br />
    3. http 폼 수정<br /> -->
    <!-- <br /><br /><br /><br /><br /><br /> -->
    <form action="http://111.111.1.247" method="post" id="SendForm">
      <table>
        <tr>
          <td>Direction</td>

          <td>
            <select name="Direction" id="Direction">
              <option value="REQ">Request</option>
              <option value="RES">Response</option>
            </select>
          </td>
        </tr>

        <tr>
          <td>Command ID</td>
          <td>
            <select onchange="SetCommand()" id="CommandId">
              <option value="0">Select</option>
              <option value="1">1:CHECK</option>
              <option value="2">2:TRIGGER</option>
              <option value="3">3:LOG</option>
              <option value="4">4:CONFIG</option>
              <option value="5">5:FUNC</option>
              <option value="6">6:RESP</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>Command</td>
          <td><input type="text" name="Command" id="Command" /></td>
        </tr>
        <tr>
          <td>Data</td>
          <td><div id="DATADIV"></div></td>
        </tr>
        <tr>
          <td>
            <input type="button" value="submit_res" onclick="CheckFormRes();" />
            <input type="button" value="Refresh" onclick="readTextFile();" />
          </td>
        </tr>
      </table>
    </form>
    <div id="log"></div>
    <pre id="Response"></pre>
  </body>
</html>

    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/")
def read_root(req: Request):
    return generate_html_response2("http://localhost/")


@app.get("/log")
def read_root(req: Request):
    return generate_html_response("log.txt")


@app.get("/log.txt")
def read_root(req: Request):
    logpath = "log.txt"
    with open(logpath, "r")as log:
        return [i + "<br> "for i in log.readlines()]


@app.get("/reslog")
def read_root(req: Request):
    # logpath = "/home/test/Django/fastapi/log.txt"
    # with open(logpath, "r")as log:
    return generate_html_response("reslog.txt")


@app.get("/reslog.txt")
def read_root(req: Request):
    logpath = "reslog.txt"
    with open(logpath, "r")as log:
        return [i + "<br> "for i in log.readlines()]


# @app.get("/")
# def home():
#     return "server is running"


@app.post("/")
async def create_item(req: Request):
    # 리퀘스트 바디데이터 정의
    bodydata = await req.json()

    # ----------------------데이터저장하기-------------

    filename = "sample"
    file_ext = ".json"
    uniq = 1
    output_path = 'data/%s%s' % (filename, file_ext)
    # 동일한 값 존재시 +1
    while os.path.exists(output_path):
        # 파일명(1) 파일명(2)...
        output_path = 'data/%s(%d)%s' % (filename, uniq, file_ext)
        uniq += 1

    with open(output_path, 'w+', encoding='utf-8') as file:
        json.dump(bodydata, file, indent="\t")
    # ---------------------로그남기기-----------------
    log_path = "log.txt"
    with open(log_path, 'a', encoding='utf-8') as log:
        now = datetime.now()
        nowdate = str(now.year)+"/" + str(now.month)+"/" + str(now.day) + \
            "/" + str(now.hour)+":" + str(now.minute) + \
            ":" + str(now.second) + "  "
        log.write(nowdate+filename+"("+str(uniq-1)+")" +
                  file_ext+"  "+str(bodydata) + "\n")
        log.close()
    # ---------------------res로그 남기기-----------------
    res = {"Direction": "RES", "Command": "RESP",
           "STATUS": "True", "DESCRIPTION": "NULL"}
    log_path = "reslog.txt"
    with open(log_path, 'a+', encoding='utf-8') as log:
        now = datetime.now()
        nowdate = str(now.year)+"/" + str(now.month)+"/" + str(now.day) + \
            "/" + str(now.hour)+":" + str(now.minute) + \
            ":" + str(now.second) + "  "
        log.write(nowdate+str(res)+"  " + "\n")
        log.close()

    # ----------------------------RES 리턴
    return res
