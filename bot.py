import os
from telegram.ext import ApplicationBuilder
from database import create_tables, add_user
from admin import admin_handlers
TOKEN = "8790701693:AAHfsOlGQVqp4zNLsgcs9Racjrk99U3bN2M"
def main():
    create_tables()
    application = ApplicationBuilder().token(TOKEN).build()
    for handler in admin_handlers:
        application.add_handler(handler)
    print("Bot is running...")
    application.run_polling()
if __name__ == "__main__":
    main()
