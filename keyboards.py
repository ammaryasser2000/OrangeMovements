from telegram import ReplyKeyboardMarkup

def main_menu():

    keyboard = [

        ["🔔 المراقبة"],

        ["💎 الاشتراك", "👤 حسابي"],

        ["🌍 تغيير اللغة"],

        ["📞 التواصل مع الإدارة"]

    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
