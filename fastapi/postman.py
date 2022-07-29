import requests
import random

num = random.random()

samplejson = {
    "direction": "REQ",
    "Command": "TRIG",
    "TRIGGER_ID": 1,
    "LOG_ID": 1
}

url = "http://127.0.0.1:8000"

response = requests.post(url, json=samplejson)

print(response.status_code)

print(response.content)
