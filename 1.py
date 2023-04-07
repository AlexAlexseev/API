import telegram

TELEGRAM_TOKEN = '520467LWjl8e0p3uA'  # Добавьте токен в код (не делайте так в реальных проектах!)
CHAT_ID = '282'  # Укажите chat_id

bot = telegram.Bot(token=TELEGRAM_TOKEN)
message = 'Prefere ellerni superfluon ol nenion lerni'
def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

send_message(message)