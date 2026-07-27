import os
from telegram.ext import ApplicationBuilder
from database import create_tables, add_user
from admin import admin_handlers
# التوكن الخاص بالبوت مباشرة
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
def main():
    # إنشاء الجداول عند البدء
    create_tables()
    # بناء تطبيق البوت باستخدام التوكن
    application = ApplicationBuilder().token(TOKEN).build()
    # إضافة أوامر المشرفين المستوردة من ملف admin.py
    for handler in admin_handlers:
        application.add_handler(handler)
    print("Bot is running...")    
    # تشغيل البوت
    application.run_polling()
if __name__ == "__main__":
    main()
