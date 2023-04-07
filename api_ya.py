import requests
import os

from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
OAuth = os.getenv('OAuth')

url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {OAuth}'}
payload = {'from_date': 1549962000}

# Делаем GET-запрос к эндпоинту url с заголовком headers и параметрами params
homework_statuses = requests.get(url, headers=headers, params=payload)

# Печатаем ответ API в формате JSON
# print(homework_statuses.text)

# А можно ответ в формате JSON привести к типам данных Python и напечатать и его
pprint(homework_statuses.json())