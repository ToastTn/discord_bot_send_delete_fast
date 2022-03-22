import requests
import time
import json 
import re 


welcome ='''                                                                                                       _ _                   
 _____ _____ ____  _____    _____ __ __            _   _                  _    _       _   _ _       _| | |_ ___ ___ ___ ___ 
|     |  _  |    \|   __|  | __  |  |  |   ___ ___| |_| |___    _ _ _ ___| |  | |_ ___| |_|_| |_ ___|_     _|_  |_  |_  |  _|
| | | |     |  |  |   __|  | __ -|_   _|  | . | .'| . | | . |  | | | | -_| |  | '_| -_|  _| | . | .'|_     _| | |  _|_  |_  |
|_|_|_|__|__|____/|_____|  |_____| |_|    |  _|__,|___|_|___|  |_____|___|_|  |_,_|___|_| |_|___|__,| |_|_|   |_|___|___|___|
                                          |_|                                                                                '''


def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    r = requests.post(url, data=data, headers=header)
    print(r.status_code)
    data = json.loads(r.text)
    message_id = data["id"]
    url_del = url + "/" + message_id
    
    r_del = requests.delete(url_del,headers=header)
    print(r_del.status_code)
    

def start_bot(token,channel_id):
    while True:
        sendMessage(token,channel_id,"msg test")
        time.sleep(60)

test_id = "948177388343287868"
my_token = "ODUzMzAyMjA0MzA3MzQxMzI3.YhaXig.TRdZsiYtGLwbImMUPo7eFABuFcI"
print(welcome)
start_bot(my_token,test_id)

 