import json


with open('/home/test/Coding_test/mysite/media/result/test.json') as f:
    data_dic = json.load(f)


def printJsonValue(data_dic):
    for key, val in data_dic.items():
        # dircetion 분석
        if (key == "direction"):
            if(val == "REQ"):
                print(val, "메시지를 수신했습니다.")
            else:
                print(val, "메시지를 응답합니다.")

        # command ID 분석
        elif (key == "CommandID"):
            if(val == 1):
                print("ID :", val, "TARGET: CONNECTION")
            elif(val == 2):
                print("ID :", val, "TARGET: GNSS")
            elif(val == 3):
                print("ID :", val, "TARGET: TIME SYNC")
            elif(val == 4):
                print("ID :", val, "TARGET: C2X")

        elif (key == "Command"):
            if(val == "TRIG"):
                print(key, "는", val, "입니다")
        else:
            print(key, "는", val, "입니다")

    return 0


k = printJsonValue(data_dic)
