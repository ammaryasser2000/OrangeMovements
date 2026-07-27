import asyncio
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from monitor import monitor_loop
from sources import IVAS, OrangeCarrier
ADMIN_IDS = [8907883947]  # الآيدي الخاص بك
subscriptions = {}
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in ADMIN_IDS or (user_id in subscriptions and subscriptions[user_id] > datetime.now()):
        await update.message.reply_text("🚀 أهلاً بك! اشتراكك ساري.\nاستخدم الأمر /movements لعرض حركات الموقعين (IVAS و Orange) معاً.")
    else:
        await update.message.reply_text("عذراً، اشتراكاتك غير سارية أو منتهية. يرجى التواصل مع المشرف لتفعيل الاشتراك.")
async def show_movements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not (user_id in ADMIN_IDS or (user_id in subscriptions and subscriptions[user_id] > datetime.now())):
        await update.message.reply_text("❌ هذا الأمر يتطلب اشتراكاً سارياً.")
        return
    await update.message.reply_text("⏳ جاري جلب الحركات والدول من موقعي IVAS و Orange Carrier...")    
    response_text = ""    
    # 1. جلب حركات IVAS
    try:
        ivas = IVAS("ammaryasser2019@gmail.com", "7700208345Ab")
        await ivas.login()
        ivas_data = await ivas.get_live_movements()
        await ivas.close()       
        if ivas_data:
            response_text += "📊 **حركات موقع IVAS:**\n" + "\n".join(ivas_data[:5]) + "\n\n"
        else:
            response_text += "📊 **حركات موقع IVAS:** لا توجد حركات حالياً.\n\n"
    except Exception as e:
        response_text += f"📊 **حركات موقع IVAS:** خطأ أثناء الجلب ({e})\n\n"
    # 2. جلب حركات Orange Carrier
    try:
        orange = OrangeCarrier("ammaryasser2019@gmail.com", "7700208345Ab$")
        await orange.login()
        orange_data = await orange.get_dashboard_movements()
        await orange.close()       
        if orange_data:
            response_text += "🟧 **حركات موقع Orange Carrier:**\n" + "\n".join(orange_data[:5])
        else:
            response_text += "🟧 **حركات موقع Orange Carrier:** لا توجد حركات حالياً."
    except Exception as e:
        response_text += f"🟧 **حركات موقع Orange Carrier:** خطأ أثناء الجلب ({e})"

    await update.message.reply_text(response_text, parse_mode="Markdown")

async def add_subscriber(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMIN_IDS:
        return
    try:
        args = context.args
        target_user_id = int(args[0])
        days = int(args[1])
        subscriptions[target_user_id] = datetime.now() + timedelta(days=days)
        await update.message.reply_text(f"✅ تم تفعيل الاشتراك للمستخدم {target_user_id} لمدة {days} يوم.")
    except:
        await update.message.reply_text("خطأ. استخدم: /add [User_ID] [عدد_الأيام]")
def main()
    app = ApplicationBuilder().token("8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("movements", show_movements))
    app.add_handler(CommandHandler("add", add_subscriber))
    loop = asyncio.get_event_loop()
    loop.create_task(monitor_loop())
    print("Bot is running with both sites monitoring...")
    app.run_polling()
if __name__ == "__main__":
    main()
