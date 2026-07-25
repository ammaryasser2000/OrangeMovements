import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M")

# ضع Telegram ID 8907883947
ADMIN_IDS = [e459b21995d2c3f98a86368c90a2efe0]

# مدة الاشتراكات بالأيام
WEEK_SUBSCRIPTION = 7
MONTH_SUBSCRIPTION = 30

# اسم البوت
BOT_NAME = "Orange Movements"

# لغات البوت
LANGUAGES = {
    "ar": "العربية",
    "en": "English",
    "bn": "বাংলা"
}
