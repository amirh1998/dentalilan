import requests
from bs4 import BeautifulSoup
import os

URL = "SITE_LINKI_BURAYA"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

# Örnek: sayfa başlığını kontrol eder
current_info = soup.get_text(" ", strip=True)[:1000]

old_info = ""
if os.path.exists("old.txt"):
    with open("old.txt", "r", encoding="utf-8") as f:
        old_info = f.read()

if current_info != old_info:
    send_message("Sitede güncelleme var:\n\n" + URL)
    with open("old.txt", "w", encoding="utf-8") as f:
        f.write(current_info)
