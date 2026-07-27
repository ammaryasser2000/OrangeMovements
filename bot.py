import os
from telegram.ext import ApplicationBuilder
from config import TOKEN
from database import create_tables, add_user
from admin import admin_handlers
def main():
    # إنشاء الجداول عند البدء
    create_tables()
    # بناء تطبيق البوت باستخدام التوكن المستورد من ملف config
    application = ApplicationBuilder().token(TOKEN).build()
    # إضافة أوامر المشرفين المستوردة من ملف admin.py
    for handler in admin_handlers:
        application.add_handler(handler)
    print("Bot is running...")    
    # تشغيل البوت
    application.run_polling()
if __name__ == "__main__":
    main()
