import qrcode
import pandas as pd
import os
from PIL import Image

checkbox_type = 1
# df = pd.read_excel('data/Бз-4.xlsx')
df = pd.read_excel('data/2 вариант.xlsx')
dir_path = 'data'

if checkbox_type == 0:
    # получаем список групп
    lst_groups = df['Группа'].unique()

    for group in lst_groups:
        # фильтруем датафрейм по названию группы
        group_df = df[df['Группа'] == group]

        for row in group_df.itertuples():
            # получаем строку с фио
            fio = f'{row[1]} {row[2]} {row[3]}'
            # Создаем строку которую будем сохранять
            qr_str = f'{fio} |\n' \
                     f'{row[5]} |\n' \
                     f'{row[6]} |\n' \
                     f'результат: {row[7]}'
            qr = qrcode.QRCode(box_size=2) # создаем экземпляр класса
            qr.add_data(qr_str) # добавляем данные
            #создаем картинку
            img = qr.make_image(fill_color="black", back_color="white")
            # меняем размер
            img = img.resize((110, 110))
            # проверяем наличие папки с названием группы, если ее нет то создаем и сохраняем файл
            if os.path.isdir(f'{dir_path}/{group}'):
                img.save(f'{dir_path}/{group}/{fio}.png')
            else:
                os.mkdir(f'{dir_path}/{group}')
                img.save(f'{dir_path}/{group}/{fio}.png')
elif checkbox_type == 1:
    # перебираем список
    for row in df.itertuples():
        id_qr = row[1] # получаем значение первой колонки по которой будут различаться колонки
        print(row)
        #создаем строку для qr кода
        qr_str = '\n'.join(row[1:])
        qr = qrcode.QRCode(box_size=2)  # создаем экземпляр класса
        qr.add_data(qr_str)  # добавляем данные
        # создаем картинку
        img = qr.make_image(fill_color="black", back_color="white")
        # меняем размер
        img = img.resize((110, 110))
        # проверяем наличие такого файла
        if os.path.isfile(f'{dir_path}/{id_qr}.png'):
            # если такой файл есть то добавляем постфикс в виде индекса строки
            img.save(f'{dir_path}/{id_qr}_{row[0]}.png')
        else:
            img.save(f'{dir_path}/{id_qr}.png')


