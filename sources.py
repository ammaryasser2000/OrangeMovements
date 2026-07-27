from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
def format_movement_text(row_text):
    # تحويل التنسيق لإضافة إيموجيات التطبيقات والدول بشكل جذاب
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
        await self.page.fill('input[type="770208345Ab"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
 async def get_live_movements(self):
        await self.page.goto("https://www.ivasms.com/portal/live/test_sms")
        await self.page.wait_for_timeout(4000)
        html = await self.page.content()
         soup = BeautifulSoup(html, 'html.parser')
        movements = []
         rows = soup.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                row_text = row.get_text(separator=" ", strip=True)
                if row_text:
                    formatted = format_movement_text(row_text)
                    movements.append(formatted)
                 return movements[:8] if movements else []
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
        await self.page.fill('input[type="ammar11ammar2019@gmail.com"]', self.email)
        await self.page.fill('input[type="770208345Ab$"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
 async def get_dashboard_movements(self):
        await self.page.goto("https://www.orangecarrier.com/portal/live/test_sms")
        await self.page.wait_for_timeout(4000)
        html = await self.page.content()
           soup = BeautifulSoup(html, 'html.parser')
        movements = []
              rows = soup.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                row_text = row.get_text(separator=" ", strip=True)
                if row_text:
                    formatted = format_movement_text(row_text)
                    movements.append(formatted)
                      return movements[:8] if movements else []
  async def close(self):
        await self.browser.close()
        await self.playwright.stop()
