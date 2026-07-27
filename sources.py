from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
def format_movement_text(row_text):
    text = row_text.lower()
    app_icon = "📱"
    if "whatsapp" in text:
        app_icon = "🟢 WhatsApp"
    elif "facebook" in text:
        app_icon = "🔵 Facebook"
    elif "apple" in text:
        app_icon = "🍏 Apple"
    elif "telegram" in text:
        app_icon = "✈️ Telegram"
    elif "google" in text:
        app_icon = "🌐 Google"
    elif "samsung" in text:
        app_icon = "📱 Samsung"
    elif "bigo" in text:
        app_icon = "🔥 Bigo"
      return f"🏳️ {row_text} | {app_icon} High Traffic 🔥"
class IVAS:
    def __init__(self, email, password):
        self.email = email
        self.password = password
 async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        self.page = await self.browser.new_page()
        await self.page.goto("https://www.ivasms.com/login")
        await self.page.fill('input[type="ammar11ammar2019@gmail.com"]', self.email)
        await self.page.fill('input[type="7700208345Ab"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
 async def get_live_movements(self):
        await self.page.goto("https://www.ivasms.com/portal/live/test_sms")
        await self.page.wait_for_timeout(5000)
        html = await self.page.content()
         soup = BeautifulSoup(html, 'html.parser')
        movements = []
             # البحث في الصفوف أو العناصر التي قد تحتوي على بيانات الحركات
        elements = soup.find_all(['tr', 'div', 'li'])
        for el in elements:
            text = el.get_text(separator=" ", strip=True)
            # استبعاد النصوص القصيرة جداً أو العامة والتركيز على محتوى الحركات
            if len(text) > 15 and ("traffic" in text.lower() or "sms" in text.lower() or "-" in text or ":" in text):
                if text not in movements:
                    movements.append(format_movement_text(text))
                 return movements[:8] if movements else ["لا توجد بيانات حالية في الجدول"]
  async def close(self):
        await self.browser.close()
        await self.playwright.stop()
class OrangeCarrier:
    def __init__(self, email, password):
        self.email = email
        self.password = password
  async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True, 
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        self.page = await self.browser.new_page()
          await self.page.goto("https://www.orangecarrier.com/login")
        await self.page.fill('input[tself.ammar11ammar2019@gmail.com "]', self.email)
        await self.page.fill('input[type="770208345Ab$"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
  async def get_dashboard_movements(self):
        await self.page.goto("https://www.orangecarrier.com/portal/live/test_sms")
        await self.page.wait_for_timeout(5000)
        html = await self.page.content()
            soup = BeautifulSoup(html, 'html.parser')
        movements = []
              # البحث الشامل في العناصر لجلب الحركة بشكل مباشر
        elements = soup.find_all(['tr', 'div', 'li'])
        for el in elements:
            text = el.get_text(separator=" ", strip=True)
            if len(text) > 15 and ("traffic" in text.lower() or "sms" in text.lower() or "-" in text or ":" in text):
                if text not in movements:
                    movements.append(format_movement_text(text))
                     return movements[:8] if movements else ["لا توجد بيانات حالية في الجدول"]
  async def close(self):
        await self.browser.close()
        await self.playwright.stop()
