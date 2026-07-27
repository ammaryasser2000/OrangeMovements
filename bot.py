from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from config import 8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M
from database import create_tables, add_user
from admin import admin_handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(
        user.id,
        user.username,
        user.full_name
    )
    keyboard = [
        ["🇸🇦 العربية"],
        ["🇬🇧 English"],
        ["🇧🇩 বাংলা"],
    ]
    await update.message.reply_text(
        "🌍 اختر اللغة\n\nChoose Language\n\nভাষা নির্বাচন করুন",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        ),
    )
async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🇸🇦 العربية":
        await update.message.reply_text("✅ تم اختيار العربية")
    elif text == "🇬🇧 English":
        await update.message.reply_text("✅ English Selected")
    elif text == "🇧🇩 বাংলা":
        await update.message.reply_text("✅ বাংলা নির্বাচন করা হয়েছে")
def main():
    create_tables()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            language
        )
    )
for handler in admin_handlers:
        app.add_handler(handler)

    print("✅ Orange Movements Bot Started")
    app.run_polling()
if __name__ == "__main__":
    main()
