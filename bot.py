import os
import asyncio
from playwright.async_api import async_playwright
class IVAS:
    def __init__(self):
        self.email = os.getenv("IVAS_EMAIL")
        self.password = os.getenv("IVAS_PASSWORD")
        self.browser = None
        self.page = None
        self.playwright = None
    async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        self.page = await self.browser.new_page()
        await self.page.goto(
            "https://www.ivasms.com/login",
            wait_until="domcontentloaded",
        )
        # نحتاج تحديد حقول تسجيل الدخول الفعلية للموقع.
        print("IVAS page opened")
    async def get_live_movements(self):
        await self.page.goto(
            "https://www.ivasms.com/portal/live/test_sms",
            wait_until="domcontentloaded",
        )
        await self.page.wait_for_timeout(5000)
        # هنا سنقرأ أسماء الدول/الحركة فقط
        return ["IVAS: تم فتح صفحة Live"]
class OrangeCarrier:
    def __init__(self):
        self.email = os.getenv("ORANGE_EMAIL")
        self.password = os.getenv("ORANGE_PASSWORD")
        self.browser = None
        self.page = None
        self.playwright = None
    async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        self.page = await self.browser.new_page()
        await self.page.goto(
            "https://www.orangecarrier.com/login",
            wait_until="domcontentloaded",
        )
        print("Orange page opened")
    async def get_dashboard_movements(self):
        await self.page.goto(
            "https://www.orangecarrier.com/portal/live/test_sms",
            wait_until="domcontentloaded",     )
        await self.page.wait_for_timeout(5000)
        return ["Orange: تم فتح صفحة Live"]
async def main():
    ivas = IVAS()
    orange = OrangeCarrier()
    try:
        await ivas.login()
        await orange.login()
        ivas_data = await ivas.get_live_movements()
        orange_data = await orange.get_dashboard_movements()
        print(ivas_data)
        print(orange_data)
    finally:
        if ivas.browser:
            await ivas.browser.close()
        if orange.browser:
            await orange.browser.close()
        if ivas.playwright:
            await ivas.playwright.stop()
  if orange.playwright:
            await orange.playwright.stop()
if __name__ == "__main__":
    asyncio.run(main())
