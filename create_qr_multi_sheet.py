"""
Скрипт для создания Qr кодов по папкам
"""
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.utils.exceptions import IllegalCharacterError
import json
import ast
import qrcode
import re
import os
from tkinter import messagebox
import datetime
import time
from dateutil import parser
pd.options.mode.chained_assignment = None

def extract_id_company(cell):
    """
    Для извления айди компании
    """
    if isinstance(cell,str):
        lst_org = cell.split('/')
        return lst_org[-1]



def processing_generate_data(data_file,end_folder,name_column_folder,name_qr_column,base_url):
    """
    Функция генерирующая куар и джейсон
    :param data_file:
    :param end_folder:
    :param name_column_folder:
    :param name_qr_column:
    :param base_url:
    :return:
    """

    t = time.localtime()  # получаем текущее время и дату
    current_time = time.strftime('%H_%M_%S', t)
    current_date = time.strftime('%d_%m_%Y', t)
    temp_wb = openpyxl.load_workbook(data_file)
    lst_sheets = temp_wb.sheetnames
    qr_folder = f'{end_folder}/QR по отраслям/{current_time}'  # создаем папку куда будем складывать qr по организациям
    json_folder = f'{end_folder}/JSON по отраслям/{current_time}'
    csv_folder = f'{end_folder}/CSV по отраслям/{current_time}'

    base_url = 'https://trudvsem.ru/vacancy/card/'  # базовая ссылка для формирования ссылки на вакансию
    # перебираем листы
    for name_sphere in lst_sheets:
        print(name_sphere)
        temp_df = pd.read_excel(data_file,sheet_name=name_sphere)

        if temp_df.shape[0] != 0:
            # Создаем JSON
            temp_df['Ссылка на вакансию'] = base_url + temp_df['URL_for_qr']
            if not os.path.exists(f'{json_folder}/{name_sphere}'):
                os.makedirs(f'{json_folder}/{name_sphere}')


            temp_json_df = temp_df[['Вакансия', 'Полное название работодателя', 'Зарплата']]
            temp_json_df.to_json(f'{json_folder}/{name_sphere}/{name_sphere[:25]}.json')

            # Создаем CSV
            if not os.path.exists(f'{csv_folder}/{name_sphere}'):
                os.makedirs(f'{csv_folder}/{name_sphere}')

            temp_csv_df = temp_df[['Вакансия', 'Полное название работодателя', 'Зарплата','Ссылка на вакансию']]
            temp_csv_df.to_csv(f'{csv_folder}/{name_sphere}/{name_sphere[:25]}.csv',encoding='UTF-8',sep='|',header=True,index=False)


            # Создаем QR коды
            if not os.path.exists(f'{qr_folder}/{name_sphere}'):
                os.makedirs(f'{qr_folder}/{name_sphere}')

            for row in temp_df.itertuples():
                name_file = row[5]
                qr = qrcode.QRCode(box_size=2)  # создаем экземпляр класса
                url_vac = row[48]
                finish_url = base_url + url_vac
                qr.add_data(finish_url)  # добавляем данные
                # # # создаем картинку
                img = qr.make_image(fill_color="black", back_color="white")
                # меняем размер
                img = img.resize((110, 110))
                # очищаем от запрещенных символов
                id_qr = re.sub(r'[<> :"?*|\\/]', ' ', name_file)
                id_qr = id_qr[:20]  # оставляем часть
                # проверяем наличие такого файла

                # itog_path =f'{qr_folder}/{name_company}/{id_qr}.png'
                #
                # # считаем возможную длину названия файл с учетом слеша и расширения с точкой и порядковым номером файла
                # threshold_name = 200 - (len(itog_path) + 10)
                # name_company = name_company[:threshold_name]  # ограничиваем название файла

                if os.path.isfile(f'{qr_folder}/{name_sphere}/{id_qr}.png'):
                    # если такой файл есть то добавляем постфикс в виде индекса строки
                    img.save(f'{qr_folder}/{name_sphere}/{id_qr}_{row[0]}.png')
                else:
                    img.save(f'{qr_folder}/{name_sphere}/{id_qr}.png')











if __name__ == '__main__':
    main_file = 'data/Общий файл.xlsx'
    main_end_folder = 'data/Отрасли'
    main_name_column_folder = 'Сфера деятельности'
    main_name_qr_column = 'URL_for_qr'
    main_base_url = 'https://trudvsem.ru/vacancy/card/'

    processing_generate_data(main_file,main_end_folder,main_name_column_folder,main_name_qr_column,main_base_url)
    print('Lindy Booth')