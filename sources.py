from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
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
            text = row.get_text(separator=" | ", strip=True)
            if text and ("NIGERIA" in text or "PHILIPPINES" in text or "HONDURAS" in text or "KENYA" in text or "Apple" in text or "WhatsApp" in text or "Shopee" in text):
                movements.append(f"🌐 [IVAS] {text}")                
        return movements[:5] if movements else ["🌐 [IVAS] لا توجد حركات نشطة حالياً"]
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
            text = row.get_text(separator=" | ", strip=True)
            if text:
                movements.append(f"🟧 [Orange] {text}")                
        return movements[:5] if movements else ["🟧 [Orange] لا توجد حركات نشطة حالياً"]
    async def close(self):
        await self.browser.close()
        await self.playwright.stop()
