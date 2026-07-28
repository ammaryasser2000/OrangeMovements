import asyncio
from datetime import datetime, timedelta
from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)
from config import (
    BOT_TOKEN,
    ADMIN_IDS,
    IVAS_EMAIL,
    IVAS_PASSWORD,
    ORANGE_EMAIL,
    ORANGE_PASSWORD,
)
from monitor import monitor_loop
from sources import IVAS, OrangeCarrier
subscriptions = {}
async def set_bot_commands(app):
    await app.bot.set_my_commands([
        BotCommand("start", "تشغيل البوت"),
        BotCommand("movements", "عرض الحركات"),
    ])
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   user_id = update.effective_user.id
    if (
        user_id in ADMIN_IDS
        or (
            user_id in subscriptions
            and subscriptions[user_id] > datetime.now()
        )
    ):
      await update.message.reply_text(
            "✅ أهلاً بك.\nاستخدم /movements لعرض الحركات."
        )
    else:
      await update.message.reply_text(
            "❌ اشتراكك غير مفعل.\n\n"
            "للتفعيل تواصل مع:\n"
            "@b_6_01"
        )
async def show_movements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if (
        user_id not in ADMIN_IDS
        and (
            user_id not in subscriptions
            or subscriptions[user_id] < datetime.now()
        )
    ):
      await update.message.reply_text(
            "❌ اشتراكك غير مفعل."
        )
        return
   await update.message.reply_text("⏳ جاري جلب الحركات...")
    response = ""
    try:
        ivas = IVAS(
            IVAS_EMAIL,
            IVAS_PASSWORD
        )
      await ivas.login()
      data = await ivas.get_live_movements()         await ivas.close()
     response += "🟠 IVAS\n\n"
        if data:
            response += "\n".join(data[:10])
        else:
            response += "لا توجد حركات"
  except Exception as e:
       response += f"IVAS ERROR\n{e}"
    response += "\n\n"
    try:
        orange = OrangeCarrier(
            ORANGE_EMAIL,
            ORANGE_PASSWORD
        )
    await orange.login()
      data = await orange.get_dashboard_movements()
        await orange.close()
       response += "🟧 OrangeCarrier\n\n"
        if data:
            response += "\n".join(data[:10])
        else:
            response += "لا توجد حركات"
   except Exception as e:
        response += f"Orange ERROR\n{e}"
   await update.message.reply_text(response)
async def add_subscriber(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return
    try:
     target = int(context.args[0])
     days = int(context.args[1])
     subscriptions[target] = (
            datetime.now() + timedelta(days=days)
        )
        await update.message.reply_text(
            "✅ تم التفعيل."
        )
   except:
       await update.message.reply_text(
            "/add user_id days"
        )
async def post_init(app):
    await set_bot_commands(app)
    asyncio.create_task(
        monitor_loop(app.bot)
    )
def main():
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )
    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("movements", show_movements)
    )

    app.add_handler(
        CommandHandler("add", add_subscriber)
    )
    print("Orange Movements Started")
    app.run_polling()
if __name__ == "__main__":
    main()
