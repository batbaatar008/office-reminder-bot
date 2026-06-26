import os
import sys
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
JOB_TYPE = os.environ.get("JOB_TYPE", "evening")

MESSAGE_THREAD_ID = 4

REPORT_LINK = "https://dsedn-my.sharepoint.com/:x:/g/personal/batbaatar_dsedn_mn/IQDrufGpU0agS6qPGZKJ3gTiAa0ZEF-geadYdU9juHaboQU?rtime=fK8Rv7zQ3kg"

EMPLOYEES = [
    "Мөнхбат",
    "Энхтөр",
    "Төгөлдөр",
    "Ариунжаргал",
    "Золзаяа",
    "Батбаатар",
    "Баярсайхан",
]

def today_mongolia():
    mn_time = datetime.now(timezone.utc) + timedelta(hours=8)
    return mn_time.strftime("%Y-%m-%d")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": MESSAGE_THREAD_ID,
        "text": text,
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print("Telegram message sent")

def basic_message():
    messages = {
        "morning": f"""🌅 Өглөөний мэнд!

Өчигдөр хийсэн ажлаа марталгүй тэмдэглээрэй. Өчигдрийн ахиц бол өнөөдрийн ажлын сайн эхлэл шүү 💪

📝 Ажлын тэмдэглэл:
{REPORT_LINK}""",

        "noon": f"""☀️ Өдрийн мэнд!

Үдээс өмнө хийсэн ажлуудаа товч тэмдэглээд аваарай. Жижиг ахиц бүр чухал шүү ✅

📝 Ажлын тэмдэглэл:
{REPORT_LINK}""",

        "evening": f"""🌇 Ажлын өдөр дуусах дөхөж байна.

Өнөөдрийн хийсэн ажлын тэмдэглэлээ хөтлөөрэй. Өнөөдрөө цэгцэлбэл маргааш илүү амар эхэлнэ 🚀

📝 Ажлын тэмдэглэл:
{REPORT_LINK}""",
    }

    return messages.get(JOB_TYPE)

def report_check_message():
    # Одоогоор Excel унших хэсгийг дараагийн алхамд залгана.
    # Энд түр placeholder байдлаар явуулж байна.
    today = today_mongolia()

    return f"""📊 Тайлан шалгах сануулга

Огноо: {today}

Ажлын тэмдэглэлээ бөглөөгүй бол одоо бөглөөрэй. Дараагийн хувилбарт бот энэ Excel-ийг өөрөө уншаад хэн бөглөөгүйг нэрээр нь гаргана 🤖

📝 Ажлын тэмдэглэл:
{REPORT_LINK}"""

if JOB_TYPE in ["morning", "noon"]:
    send_telegram(basic_message())

elif JOB_TYPE == "evening":
    send_telegram(basic_message())
    send_telegram(report_check_message())

else:
    print(f"Unknown JOB_TYPE: {JOB_TYPE}")
    sys.exit(1)
