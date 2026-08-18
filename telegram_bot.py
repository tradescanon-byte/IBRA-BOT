import os, requests
BOT_TOKEN=os.getenv("BOT_TOKEN","")
CHAT_ID=os.getenv("CHAT_ID","")
def send_message(text):
    url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r=requests.post(url,json={"chat_id":CHAT_ID,"text":text},timeout=15)
    return r.json()
