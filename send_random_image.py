
import requests
from telegram import Bot
from pprint import pprint

TELEGRAM_TOKEN = '6147939461:AAGLYjzvSdiUUCs6n-o2m9lYBMLLBh4KG54'
bot = Bot(token=TELEGRAM_TOKEN)

URL = 'https://api.thecatapi.com/v1/images/search'

# Сделаем GET-запрос к API
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python
response = requests.get(URL).json()

# Рассмотрим структуру и содержимое переменной response
pprint(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0])) 

# chat_id = 811987925
# text = 'Вам телеграмма!'
# # Отправка сообщения
# bot.send_message(chat_id, text)
# # Отправка изображения
# bot.send_photo(chat_id, URL)