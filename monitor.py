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
    print("Starting monitoring loop for websites...")
    while True:
        try:
            # 1. فحص الموقع الأول IVAS (ضع بريدك وكلمة المرور بين علامات التنصيص)
            ivas = IVAS("ammar11ammar2019@gmail.com", "7700208345Ab")
            await ivas.login()
            ivas_data = await ivas.open_live()
            await ivas.close()
     if ivas_data:
                await send_telegram_alert("📊 تم فحص حساب IVAS وسحب البيانات بنجاح!")
            # 2. فحص الموقع الثاني OrangeCarrier (ضع بريدك وكلمة المرور بين علامات التنصيص)
            orange = OrangeCarrier("ammar11ammar2019@gmail.com", "7700208345Ab$")
            await orange.login()
            orange_data = await orange.dashboard()
            await orange.close()           
            if orange_data:
                await send_telegram_alert("📊 تم فحص حساب OrangeCarrier وسحب البيانات بنجاح!")           
        except Exception as e:
            print("Monitor Loop Error:", e)
        # الفحص كل 60 ثانية (دقيقة واحدة)
        await asyncio.sleep(60)
