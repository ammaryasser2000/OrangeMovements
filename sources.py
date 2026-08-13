import os
from datetime import datetime, timezone
from playwright.async_api import async_playwright


class IVAS:
    def __init__(self):
        self.email = os.getenv("IVAS_EMAIL")
        self.password = os.getenv("IVAS_PASSWORD")
        self.playwright = None
        self.browser = None
        self.page = None

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

        # selectors الصحيحة حسب الصفحة التي أرسلتها
        await self.page.fill("#card-email", self.email)
        await self.page.fill("#card-password", self.password)

        await self.page.click('button[name="submit"]')

        await self.page.wait_for_timeout(5000)

    async def get_live_movements(self):
        await self.page.goto(
            "https://www.ivasms.com/portal/live/test_sms",
            wait_until="domcontentloaded",
        )

        await self.page.wait_for_timeout(5000)

        rows = await self.page.locator("#LiveTestSMS tr").all()

        result = []

        for row in rows:
            try:
                # نأخذ اسم الدولة + الرنج فقط
                name = await row.locator("h6").inner_text()

                name = " ".join(name.split())

                if name and name not in result:
                    result.append(name)

            except Exception:
                continue

        return result

    async def close(self):
        if self.browser:
            await self.browser.close()

        if self.playwright:
            await self.playwright.stop()
