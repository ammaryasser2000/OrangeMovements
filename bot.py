async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != 8907883947:
        return
    if len(context.args) != 1:
        await update.message.reply_text("Use: /week USER_ID")
        return
    user_id = int(context.args[0])
    add_subscription(user_id, "week")
    await update.message.reply_text("Done: Weekly added.")

async def month(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != 8907883947:
        return
    if len(context.args) != 1:
        await update.message.reply_text("Use: /month USER_ID")
        return
    user_id = int(context.args[0])
    add_subscription(user_id, "month")
    await update.message.reply_text("Done: Monthly added.")

# قم بإضافة هذه الأسطر مع بقية الـ handlers الموجودة لديك في bot.py
application.add_handler(CommandHandler("week", week))
application.add_handler(CommandHandler("month", month))
