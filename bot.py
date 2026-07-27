import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from monitor import monitor_loop
user_language = {}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_language[user_id] = "ar"
    await update.message.reply_text("مرحباً بك! تم تشغيل بوت المراقبة بنجاح.")
def main():
    app = ApplicationBuilder().token("8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M").build()    
    app.add_handler(CommandHandler("start", start))   
    loop = asyncio.get_event_loop()
    loop.create_task(monitor_loop())
    print("Bot is running...")
    app.run_polling()
if __name__ == "__main__":
    main()
