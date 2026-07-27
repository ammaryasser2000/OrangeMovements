import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import create_tables, add_user
# استيراد معالجات الأدمن (week, month)
try:
    from admin import admin_handlers
except ImportError:
    admin_handlers = []
# محاولة استيراد معالجات المراقبة وحركة المرور إن وجدت
try:
    from monitor import monitor_handlers
except ImportError:
    monitor_handlers = []
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
# دالة البداية والترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id)
    await update.message.reply_text(
        "🚀 أهلاً بك في بوت حركات أورانج وسجلات المكالمات\n\n"
        "📋 الأوامر المتاحة:\n"
        "/start - عرض هذه الرسالة\n"
        "/traffic - عرض حركة المرور وسجلات المكالمات\n"
        "/week [id] - تفعيل اشتراك أسبوعي (أدمن)\n"
        "/month [id] - تفعيل اشتراك شهري (أدمن)"
    )
# دالة حركة المرور
async def traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 **قسم حركة المرور وسجلات المكالمات:**\n"
        "النظام يعمل ويراقب البيانات الحالية."
    )
def main():
    # إنشاء جداول قاعدة البيانات
    create_tables()    
    # بناء التطبيق
    application = ApplicationBuilder().token(TOKEN).build()    
    # إضافة الأوامر الأساسية وحركة المرور
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("traffic", traffic))    
    # إضافة أوامر الأدمن
    for handler in admin_handlers:
        application.add_handler(handler)        
    # إضافة أوامر المراقبة إن وجدت
    for handler in monitor_handlers:
        application.add_handler(handler)     
    print("Bot is fully running with all file handlers...")
    application.run_polling()
if __name__ == "__main__":
    main()
