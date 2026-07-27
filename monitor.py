from playwright.async_api import async_playwright

class IVAS:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    async def login(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True
        )
        self.page = await self.browser.new_page()

        await self.page.goto(
            "https://www.ivasms.com/login"
        )
        await self.page.fill(
            'input[type="ammar11ammar2019@gmail.com"]',
            self.email
        )
        await self.page.fill(
            'input[type="7700208345Ab"]',
            self.password
        )
        await self.page.click(
            'button[type="submit"]'
        )
        await self.page.wait_for_timeout(5000)
    async def open_live(self):
        await self.page.goto(
            "https://www.ivasms.com/portal/live/test_sms"
        )
        await self.page.wait_for_timeout(3000)
        html = await self.page.content()
        return html
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
            headless=True
        )
        self.page = await self.browser.new_page()
        await self.page.goto(
            "https://www.orangecarrier.com/login"
        )
        await self.page.fill(
            'input[type="ammar11ammar2019@gmail.com"]',
            self.email
        )
        await self.page.fill(
            'input[type="7700208345Ab$"]',
            self.password
        )
        await self.page.click(
            'button[type="submit"]'
        )
        await self.page.wait_for_timeout(5000)
    async def dashboard(self):
        html = await self.page.content()
        return html
    async def close(self):
        await self.browser.close()
        await self.playwright.stop()
