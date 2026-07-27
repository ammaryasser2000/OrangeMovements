import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import create_tables, add_user
# محاولة استيراد الأوامر المتقدمة أو ملف الأدمن إن وجد
try:
    from admin import admin_handlers
except ImportError:
    admin_handlers = []
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
# دالة الترحيب الأساسية عند إرسال /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id)  # تسجيل المستخدم في القاعدة إذا كانت الدالة تدعم ذلك
    await update.message.reply_text(
        "أهلاً بك في بوت حركات أورانج 🚀\n\n"
        "الأوامر المتاحة:\n"
        "/start - بدء البوت وعرض القائمة\n"
        "/traffic - عرض حركة المرور وسجلات المكالمات"
    )
# دالة حركة المرور وسجلات المكالمات
async def traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 جاري جلب أحدث بيانات حركة المرور وسجلات المكالمات من أورانج...")
def main():
    # إنشاء الجداول في قاعدة البيانات
    create_tables()    
    # بناء تطبيق تيليجرام
    application = ApplicationBuilder().token(TOKEN).build()    
    # إضافة الأوامر الأساسية
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("traffic", traffic))    
    # إضافة بقية المعالجات من ملف admin إن وجدت
    for handler in admin_handlers:
        application.add_handler(handler)        
    print("Bot is running...")
    application.run_polling()
if __name__ == "__main__":
    main()
