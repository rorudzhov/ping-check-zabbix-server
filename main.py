import datetime
import json
import os
import requests
import os.path
import CONFIG as CFG

# READ LAST STATES
STATES = None
with open(file="states.json", mode="r") as file:
    STATES = json.loads(file.read())
# ----------|----------|----------

def sendMsg(message: str):
    response = requests.get(
        f"https://api.telegram.org/bot{CFG.TG_TOKEN}/sendMessage?chat_id={CFG.TG_CHAT_ID}&text={message}")
    if response.status_code == 200:
        print("Message has been send")
    else:
        print("When you send an error has occurred")
        print(f'{str(response.status_code)} - {json.loads(response.text)["description"]}' )

def ping(address: str) -> bool:
    response = os.system(f"ping -c 4 {address}")
    if response == 0:
        return True
    else:
        return False


def main():

    result = ping(CFG.HOST)

    # IF HOST IS UNAVALIABLE
    if result is False and STATES["last_check"] is True:
        STATES["last_check"] = False
        sendMsg(CFG.PROBLEM_MESSAGE.format(datetime=datetime.datetime.now().strftime("%H:%M:%S | %Y.%m.%d"),
                                       host=CFG.HOST))
    # ----------|----------|----------

    # IF PROBLEM OF HOST HAS BEEN RESOLVED
    if result is True and STATES["last_check"] is False:
        STATES["last_check"] = True
        sendMsg(CFG.RESOLVE_MESSAGE.format(datetime=datetime.datetime.now().strftime("%H:%M:%S | %Y.%m.%d"),
                                       host=CFG.HOST))
    # ----------|----------|----------
    
    # WRITE LAST STATES
    with open(file="states.json", mode="w") as file:
            file.write(json.dumps(STATES))
    # ----------|----------|----------


if __name__ == '__main__':
    main()
