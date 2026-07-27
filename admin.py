from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from subscriptions import add_subscription

# ضع هنا رقم حسابك في تيليجرام
ADMIN_ID = 8907883947


async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "استخدم:\n/week USER_ID"
        )
        return

    user_id = int(context.args[0])
    add_subscription(user_id, "week")
    await update.message.reply_text(
        "✅ تم إضافة اشتراك أسبوعي."
    )


async def month(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    if len(context.args) != 1:
        await update.message.reply_text(
            "استخدم:\n/month USER_ID"
        )
        return

    user_id = int(context.args[0])
    add_subscription(user_id, "month")
    await update.message.reply_text(
        "✅ تم إضافة اشتراك شهري."
    )


admin_handlers = [
    CommandHandler("week", week),
    CommandHandler("month", month),
]
            "استخدم:\n/month USER_ID"
        )
        return

    user_id = int(context.args[0])

    add_subscription(user_id, "month")

    await update.message.reply_text(
        "✅ تم إضافة اشتراك شهري."
    )


admin_handlers = [
    CommandHandler("week", week),
    CommandHandler("month", month),
]
