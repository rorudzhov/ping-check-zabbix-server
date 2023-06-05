import datetime
import os
import requests

HOST = "example.com"  # DOMAIN OR IP
TG_TOKEN = "1112223334:AABBCCDDZy7uogv5XhjLLXL1HHJEVAA1212"  # TELEGRAM TOKEN
TG_CHAT_ID = "123456562"  # YOUR CHAT ID WITH BOT

# IF YOU WANT THEN YOU CAN CHANGE TG MESSAGE
# VAR datetime IT IS CURENT DATE TIME IN VIEW "HH:MM:SS | YYYY.MM.DD"
# VAR host IT IS HOST VARIABLE

MESSAGE: str = """
❌❌❌❌❌❌❌❌❌❌❌❌
❌  MASTER PROBLEM  ❌
❌❌❌❌❌❌❌❌❌❌❌❌
TIME: {datetime}
HOST: ZABBIX MASTER SERVER - {host}
TRIGGER: ICMP: Unavailable by ICMP
LEVEL: DISASTER
"""


def sendMsg(message: str):
    requests.get(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage?chat_id={TG_CHAT_ID}&text={message}")


def ping(address: str) -> bool:
    response = os.system(f"ping -c 4 {address}")
    if response == 0:
        return True
    else:
        return False


def main():
    if ping(HOST) is False:
        sendMsg(MESSAGE.format(datetime=datetime.datetime.now().strftime("%H:%M:%S | %Y.%m.%d"),
                               host=HOST))


if __name__ == '__main__':
    main()
