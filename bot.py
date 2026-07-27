import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from database import create_tables, add_user
# استيراد معالجات الأدمن والملفات الأخرى الموجودة في مشروعك
try:
    from admin import admin_handlers
except ImportError:
    admin_handlers = []
try:
    from monitor import *
except ImportError:
    pass
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id)
    await update.message.reply_text(
        "أهلاً بك في بوت حركات أورانج 🚀\n"
        "تم تفعيل النظام بنجاح وربط كافة الملفات."
    )
def main():
    # إنشاء جداول قاعدة البيانات
    create_tables()   
    # بناء التطبيق
    application = ApplicationBuilder().token(TOKEN).build()   
    # إضافة أمر البدء
    application.add_handler(CommandHandler("start", start))    
    # إضافة جميع معالجات ملف admin والملفات الأخرى
    for handler in admin_handlers:
        application.add_handler(handler)        
    print("Bot is running with all features...")
    application.run_polling()
if __name__ == "__main__":
    main()
