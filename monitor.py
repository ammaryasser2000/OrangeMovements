import asyncio
from sources import IVAS, OrangeCarrier
from telegram import Bot
TELEGRAM_TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
CHAT_ID = 8907883947
async def send_telegram_alert(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print("Telegram Error:", e)
async def monitor_loop():
    print("Starting monitoring loop...")
    while True:
        try:
            # مثال لاستخدام IVAS مع وضع البريد وكلمة المرور بين علامات التنصيص
            ivas = IVAS("example@gmail.com", "your_password")
            await ivas.login()
            html_content = await ivas.open_live()
            await ivas.close()
                        if html_content:
                await send_telegram_alert("📊 تم فحص حركة المرور بنجاح!")
     except Exception as e:
            print("Monitor Loop Error:", e)
        
        await asyncio.sleep(60)
if __name__ == "__main__":
    asyncio.run(monitor_loop())
