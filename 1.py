from telegram.ext import Updater, Filters, MessageHandler
import telegram

TELEGRAM_TOKEN = '5204672338:AAG2OuyVBMkfZBIR-L0tUxrxLWjl8e0p3uA'  # Добавьте токен в код (не делайте так в реальных проектах!)
# CHAT_ID = '811987925'  # Укажите chat_id

# bot = telegram.Bot(token=TELEGRAM_TOKEN)

# updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
updater = Updater(token='6147939461:AAGLYjzvSdiUUCs6n-o2m9lYBMLLBh4KG54')


def say_hi(update, context):
    # Получаем информацию о чате, из которого пришло сообщение,
    # и сохраняем в переменную chat
    chat = update.effective_chat
    # В ответ на любое текстовое сообщение 
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')

# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# updater.start_polling(poll_interval=20.0) 
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle()