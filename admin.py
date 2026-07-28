from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from config import ADMIN_IDS
from subscriptions import add_subscription
async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
  if update.effective_user.id not in ADMIN_IDS:
        return
  if len(context.args) != 1:
        await update.message.reply_text(
            "Usage:\n/week USER_ID"
        )
        return
 user_id = int(context.args[0])
 add_subscription(user_id, "week")
  await update.message.reply_text(
        "✅ Weekly subscription added."
    )
async def month(update: Update, context: ContextTypes.DEFAULT_TYPE):
  if update.effective_user.id not in ADMIN_IDS:
        return
  if len(context.args) != 1:
        await update.message.reply_text(
            "Usage:\n/month USER_ID"
        )
        return
  user_id = int(context.args[0])
 add_subscription(user_id, "month")
  await update.message.reply_text(
        "✅ Monthly subscription added."
    )
admin_handlers = [
   CommandHandler("week", week),
   CommandHandler("month", month),

]
