from config import TOKEN
import yadisk
import requests
import pprint
import pandas as pd

y = yadisk.YaDisk(token=TOKEN)

if y.check_token():
    print('Токен валиден')

headers = {"Authorization": f"OAuth {TOKEN}"}
url = 'https://forms.yandex.ru/cloud/files?path=%2F7792313%2Fd87655a8a47c01d3ad13c31a0a002ddd_2023_04_14_kompleksnyi_proforien.xlsx'


import yadisk


# with open(f'data/test.xlsx', "wb") as f:
#     f.write(response.content)

#
# FILE_PATH = "ПУТЬ К ФАЙЛУ НА ЯНДЕКС.ДИСКЕ"
# DOWNLOAD_PATH = "data"
#
# # Получаем информацию о файле

# params = {"path": FILE_PATH}
response = requests.get(url, headers=headers)
pprint.pprint(response.text)

# download_url = response.json()["href"]
# #
# # # Скачиваем файл
# # response = requests.get(download_url)
# # print(response)
# with open(f'data/test.xlsx', "wb") as f:
#     f.write(response.content)

#
