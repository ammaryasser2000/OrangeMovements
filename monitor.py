import asyncio
from sources import IVAS, OrangeCarrier
from telegram import Bot
# بيانات التيليجرام والبوت
TELEGRAM_TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
CHAT_ID = 8907883947
# بيانات الدخول الخاصة بك (استبدلها بالبريد وكلمة المرور الحقيقية)
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
async def send_telegram_alert(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        print("Telegram Error:", e)
async def monitor_loop():
    print("Starting monitoring loop on Termux...")
    while True:
        try:
            # فحص IVAS وجلب البيانات الحية
            ivas = IVAS(EMAIL, PASSWORD)
            await ivas.login()
            html_content = await ivas.open_live()
            await ivas.close()            
            if html_content:
                await send_telegram_alert("📊 تم فحص صفحة حركة المرور بنجاح وجلب التحديثات!")    
        except Exception as e:
            print("Monitor Loop Error:", e)       
        # الانتظار 60 ثانية قبل الفحص القادم
        await asyncio.sleep(60)
if __name__ == "__main__":
    asyncio.run(monitor_loop())
