import os
from dotenv import load_dotenv
load_dotenv()
# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Database
DATABASE_NAME = "orange.db"
# IVAS
IVAS_EMAIL = os.getenv("ammar11ammar2019@gmail.com")
IVAS_PASSWORD = os.getenv("770208345Ab")
# Orange Carrier
ORANGE_EMAIL = os.getenv("ammar11ammar2019@gmail.com")
ORANGE_PASSWORD = os.getenv("770208345Ab$")
# Telegram Group
GROUP_ID = int(os.getenv("GROUP_ID", "-1003764162114"))
# Admin
ADMIN_IDS = [
    int(os.getenv("ADMIN_ID", "8907883947"))
]
SUPPORT_USERNAME = "@b_6_01"
CHECK_INTERVAL = 30
