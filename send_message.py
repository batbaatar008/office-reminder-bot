import os
import requests
import smtplib
from email.message import EmailMessage

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

EMAIL_RECIPIENTS = [
    "munkhbat@dsedn.mn",
    "enkhtur@dsedn.mn",
    "tuguldur@dsedn.mn",
    "ariunjargal@dsedn.mn",
    "zolzaya@dsedn.mn",
    "batbaatar@dsedn.mn",
    "bayarsaikhan@dsedn.mn",
]

JOB_TYPE = os.environ["JOB_TYPE"]

MESSAGES = {
    "telegram_morning": "Өглөөний мэнд 🌞\n\nӨдрийн төлөвлөгөөгөө гаргаарай.",
    "telegram_noon": "Сайн уу 👋\n\nӨглөөнөөс хойш хийсэн ажлаа тэмдэглээрэй.",
    "telegram_evening": "⏰ Сануулга\n\nӨнөөдрийн ажлаа марталгүй бичээрэй, амжилт 💪",
    "email_morning": "Өдрийн зорилтоо тодорхойлоод, өнөөдрийн хийх ажлаа төлөвлөөрэй.",
    "email_evening": "Өдрийн тайлангаа бөглөж, хийсэн ажлуудаа тэмдэглээрэй.",
}

EMAIL_SUBJECTS = {
    "email_morning": "Өдрийн зорилтын сануулга",
    "email_evening": "Өдрийн тайлан бөглөх сануулга",
}

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    })
    response.raise_for_status()
    print("Telegram message sent")

def send_email(subject, body):
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = ", ".join(EMAIL_RECIPIENTS)
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email sent")

if JOB_TYPE.startswith("telegram"):
    send_telegram(MESSAGES[JOB_TYPE])

elif JOB_TYPE.startswith("email"):
    send_email(EMAIL_SUBJECTS[JOB_TYPE], MESSAGES[JOB_TYPE])

else:
    raise ValueError(f"Unknown JOB_TYPE: {JOB_TYPE}")
