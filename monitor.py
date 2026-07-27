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
            ivas = IVAS("ammar11ammar2019@gmail.com", "7700208345Ab")
            await ivas.login()
            ivas_data = await ivas.get_live_movements()
            await ivas.close()            
            if ivas_data:
                await send_telegram_alert(f"📊 حركات IVAS الجديدة:\n" + "\n".join(ivas_data[:5]))
example_orange@gmail.com
            orange = OrangeCarrier("ammar11ammar2019@gmail.com", "7700208345Ab$")
            await orange.login()
            orange_data = await orange.get_dashboard_movements()
            await orange.close()            
            if orange_data:
                await send_telegram_alert(f"📊 حركات Orange الجديدة:\n" + "\n".join(orange_data[:5]))
        except Exception as e:
            print("Monitor Loop Error:", e)        
        await asyncio.sleep(60)
