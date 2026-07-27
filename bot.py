import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import create_tables, add_user
from admin import admin_handlers
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
# دالة الاستجابة لأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! بوت حركات أورانج يعمل بنجاح 🚀")
def main():
    create_tables()
    application = ApplicationBuilder().token(TOKEN).build()    
    # إضافة أمر /start للتشغيل
    application.add_handler(CommandHandler("start", start))    
    # إضافة دوال الأدمن الأخرى
    for handler in admin_handlers:
        application.add_handler(handler)        
    print("Bot is running...")
    application.run_polling()
if __name__ == "__main__":
    main()
