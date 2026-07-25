import os
from dotenv import load_dotenv

# تحميل بيانات ملف .env
load_dotenv()

# توكن البوت
BOT_TOKEN = os.getenv("e459b21995d2c3f98a86368c90a2efe0")

# آيدي الأدمن
ADMIN_IDS = [
    35259577
]

# رابط الدعم
SUPPORT = [
    "@b_6_0",
    "@b_6_01"
]

# قاعدة البيانات
DATABASE_NAME = "orange.db"

# اللغات
LANGUAGES = ["ar", "en", "bn"]
