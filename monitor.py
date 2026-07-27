import asyncio
from sources import IVAS, OrangeCarrier
from telegram import Bot
TELEGRAM_TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
GROUP_CHAT_ID = -1003764162114  # آيدي المجموعة
async def send_to_group(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(chat_id=GROUP_CHAT_ID, text=message, parse_mode="Markdown")
    except Exception as e:
        print("Telegram Group Error:", e)
async def monitor_loop():
    print("Starting monitoring loop for all countries...")
    while True:
        try:
            # 1. سحب الحركات من موقع IVAS
            ivas = IVAS("ammaryasser2019@gmail.com", "7700208345Ab")
            await ivas.login()
            ivas_data = await ivas.get_live_movements()
            await ivas.close()      
            if ivas_data:
                msg = "🌐 *موقع: IVAS*\n\n" + "\n".join(ivas_data)
                await send_to_group(msg)
            # 2. سحب الحركات من موقع Orange Carrier
            orange = OrangeCarrier("ammaryasser2019@gmail.com", "7700208345Ab$")
            await orange.login()
            orange_data = await orange.get_dashboard_movements()
            await orange.close()
                   if orange_data:
                msg = "🟧 *موقع: Orange Carrier*\n\n" + "\n".join(orange_data)
                await send_to_group(msg)       
        except Exception as e:
            print("Monitor Loop Error:", e)
  await asyncio.sleep(30)
