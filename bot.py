from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os

# قراءة التوكن من ملف .env
TOKEN = os.getenv("BOT_TOKEN")

# حفظ لغة المستخدم مؤقتًا
user_language = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🇸🇦 العربية"],
        ["🇬🇧 English"],
        ["🇧🇩 বাংলা"],
    ]

    await update.message.reply_text(
        "🌍 اختر لغتك / Choose your language / আপনার ভাষা নির্বাচন করুন",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🇸🇦 العربية":
        user_language[update.effective_user.id] = "ar"
        await update.message.reply_text("✅ تم اختيار اللغة العربية")

    elif text == "🇬🇧 English":
        user_language[update.effective_user.id] = "en"
        await update.message.reply_text("✅ English selected")

    elif text == "🇧🇩 বাংলা":
        user_language[update.effective_user.id] = "bn"
        await update.message.reply_text("✅ বাংলা নির্বাচন করা হয়েছে")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, language))

    print("Orange Movements Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
