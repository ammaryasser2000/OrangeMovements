
import requests
from bs4 import BeautifulSoup

URL = "https://www.ivasms.com/portal/live/test_sms"


def get_movements():
    try:
        response = requests.get(URL, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # حالياً نجلب النص الكامل من الصفحة
        # وفي الخطوة التالية سنحدد الجدول بدقة
        text = soup.get_text("\n", strip=True)

        return text

    except Exception as e:
        print("Monitor Error:", e)
        return None
