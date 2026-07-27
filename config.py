import os
from dotenv import load_dotenv
# تحميل بيانات ملف .env
load_dotenv()
# توكن البوت
BOT_TOKEN = os.getenv("8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M")
# قاعدة البيانات
DATABASE_NAME = os.getenv("DATABASE_NAME", "orange.db")
# بيانات IVAS
IVAS_EMAIL = os.getenv("ammar11ammar2019@gmail.com")
IVAS_PASSWORD = os.getenv("770208345Ab")
# بيانات OrangeCarrier
ORANGE_EMAIL = os.getenv("ammar11ammar2019@gmail.com")
ORANGE_PASSWORD = os.getenv("770208345Ab$")
# مدة الفحص (كل 30 ثانية)
CHECK_INTERVAL = 30
# آيديات الأدمن
ADMIN_IDS = [
    8907883947
]
# حسابات الدعم
SUPPORT = [
    "@b_6_0",
    "@b_6_01"
]

# اللغات
LANGUAGES = [
    "ar",
    "en",
    "bn"
]
