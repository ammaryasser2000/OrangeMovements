import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import create_tables, add_user
# استيراد معالجات الأدمن (الأشتراكات)
try:
    from admin import admin_handlers
except ImportError:
    admin_handlers = []
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
# دالة الترحيب وعرض الأوامر المتاحة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id)
    await update.message.reply_text(
        "أهلاً بك في بوت حركات أورانج 🚀\n\n"
        "📋 الأوامر المتاحة:\n"
        "/start - بدء البوت\n"
        "/traffic - عرض حركة المرور وسجلات المكالمات\n"
        "/week [user_id] - إضافة اشتراك أسبوعي (للأدمن)\n"
        "/month [user_id] - إضافة اشتراك شهري (للأدمن)"
    )
# دالة حركة المرور وسجلات المكالمات
async def traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 **قسم حركة المرور وسجلات المكالمات:**\n\n"
        "النظام جاهز لمراقبة الصفحة وجلب السجلات. استخدم الأوامر المتاحة أو انتظر التحديثات الفورية."
    )
def main():
    # إنشاء جداول قاعدة البيانات
    create_tables()    
    # بناء تطبيق تيليجرام
    application = ApplicationBuilder().token(TOKEN).build()    
    # إضافة الأوامر الأساسية وحركة المرور
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("traffic", traffic))    
    # إضافة أوامر الأدمن (week, month)
    for handler in admin_handlers:
        application.add_handler(handler)        
    print("Bot is fully running with all handlers...")
    application.run_polling()
if __name__ == "__main__":
    main()
