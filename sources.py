from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
class IVAS:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto("https://www.ivasms.com/login")
        await self.page.fill('input[type="ammar11ammar2019@gmail.com"]', self.email)
        await self.page.fill('input[type="7700208345Ab"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
    async def get_live_movements(self):
        await self.page.goto("https://www.ivasms.com/portal/live/test_sms")
        await self.page.wait_for_timeout(3000)
        html = await self.page.content()
        # تحليل الصفحة واستخراج الحركات والدول والخدمات
        soup = BeautifulSoup(html, 'html.parser')
        movements = []        
        # استخراج الصفوف من جدول الحركات (تأكد من هيكل الجدول في الموقع)
        rows = soup.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                text_content = row.get_text(separator=" | ", strip=True)
                movements.append(text_content)                
        return movements if movements else ["لا توجد حركات جديدة حالياً"]
    async def close(self):
        await self.browser.close()
        await self.playwright.stop()
class OrangeCarrier:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        await self.page.goto("https://www.orangecarrier.com/login")
        await self.page.fill('input[type="ammar11ammar2019@gmail.com"]', self.email)
        await self.page.fill('input[type="7700208345Ab$"]', self.password)
        await self.page.click('button[type="submit"]')
        await self.page.wait_for_timeout(5000)
    async def get_dashboard_movements(self):
        html = await self.page.content()
        soup = BeautifulSoup(html, 'html.parser')
        movements = []       
        rows = soup.find_all('tr')
        for row in rows:
            text_content = row.get_text(separator=" | ", strip=True)
            if text_content:
                movements.append(text_content) 
        return movements if movements else ["لا توجد بيانات جديدة"]
    async def close(self):
        await self.browser.close()
        await self.playwright.stop()
