from config import TOKEN
import yadisk

y = yadisk.YaDisk(token=TOKEN)

if y.check_token():
    print('Токен валиден')

y.download('https://forms.yandex.ru/cloud/files?path=%2F7792313%2Fd87655a8a47c01d3ad13c31a0a002ddd_2023_04_14_kompleksnyi_proforien.xlsx', '1.xlsx')

import requests

TOKEN = "ВАШ ТОКЕН"
FILE_PATH = "ПУТЬ К ФАЙЛУ НА ЯНДЕКС.ДИСКЕ"
DOWNLOAD_PATH = "ПУТЬ ДЛЯ СОХРАНЕНИЯ ФАЙЛА"

# Получаем информацию о файле
headers = {"Authorization": f"OAuth {TOKEN}"}
params = {"path": FILE_PATH}
response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/download", headers=headers, params=params)
download_url = response.json()["href"]

# Скачиваем файл
response = requests.get(download_url)
with open(DOWNLOAD_PATH, "wb") as f:
    f.write(response.content)
