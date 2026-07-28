import asyncio
from telegram import Bot
from config import (
    BOT_TOKEN,
    GROUP_ID,
    IVAS_EMAIL,
    IVAS_PASSWORD,
    ORANGE_EMAIL,
    ORANGE_PASSWORD,
)
from sources import IVAS, OrangeCarrier
last_sent = set()
async def send_to_group(bot, text):
    try:
        await bot.send_message(
            chat_id=GROUP_ID,
            text=text
        )
    except Exception as e:
        print(e)
async def monitor_loop(bot):
    print("Monitor Started")
    while True:
        try:
            # IVAS
            ivas = IVAS(
                IVAS_EMAIL,
                IVAS_PASSWORD
            )
    await ivas.login()
      movements = await ivas.get_live_movements()
   await ivas.close()
     for item in movements:
        if item not in last_sent:
           last_sent.add(item)
          await send_to_group(
                        bot,
                        f"🟠 IVAS\n\n{item}"
                    )
        except Exception as e:
      print("IVAS:", e)
        try:
            # OrangeCarrier
            orange = OrangeCarrier(                ORANGE_EMAIL,
                ORANGE_PASSWORD
            )
            await orange.login()
            movements = await orange.get_dashboard_movements()
            await orange.close()
            for item in movements:
              if item not in last_sent:
             last_sent.add(item)
                    await send_to_group(
                        bot,
                        f"🟧 OrangeCarrier\n\n{item}"
                    )
       except Exception as e:
print("Orange:", e)
        await asyncio.sleep(30)
