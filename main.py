import time
import requests
from secret import client_key

url = "https://discord.com/api/v8/users/@me/settings"

with open("text.txt", "r") as file:
    lines = file.readlines()

def ChangeStatus(message):
    header = {
        "authorization": client_key
    }
  
    jsonData = {
            "status": "idle",
            "custom_status": {
                "text": message
            }
    }
    request = requests.patch(url, headers=header, json=jsonData)

while True:
    for line in lines:

        ChangeStatus(line.split("\n") [0])
        time.sleep(2)


       