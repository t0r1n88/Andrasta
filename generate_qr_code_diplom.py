import qrcode
import pandas as pd
import os
from PIL import Image

df = pd.read_excel('data/Бз-4.xlsx')
dir_path = 'data'

lst_groups = df['Группа'].unique()


for group in lst_groups:
    group_df = df[df['Группа'] == group]

    for row in group_df.itertuples():
        print(row)
        print(row[2])
        fio = f'{row[1]} {row[2]} {row[3]}'
        # Создаем строку которую будем сохранять
        qr_str = f'{fio} |\n' \
                 f'{row[5]} |\n' \
                 f'{row[6]} |\n' \
                 f'результат: {row[7]}'

        qr = qrcode.QRCode(box_size=10)
        qr.add_data(qr_str)
        img = qr.make_image(fill_color="black", back_color="white")
        # меняем размер
        img = img.resize((300, 300))

        if os.path.isdir(f'{dir_path}/{group}'):
            img.save(f'{dir_path}/{group}/{fio}.png')
        else:
            os.mkdir(f'{dir_path}/{group}')
            img.save(f'{dir_path}/{group}/{fio}.png')



        # if os.path.isdir(f'{dir_path}/{group}'):
        #     print('Lindy')
        #
        #
        #     img.save(f'{dir_path}/{group}/{fio}.png')
        # else:
        #     os.mkdir(f'{dir_path}/{group}')
        #     img.save(f'{dir_path}/{group}/{fio}.png')

        # img.save(f'{fio}.png')
