import tkinter
import sys
import re
import pandas as pd
import qrcode
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time
# pd.options.mode.chained_assignment = None  # default='warn'
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller
    Функция чтобы логотип отображался"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def select_end_folder():
    """
    Функция для выбора конечной папки куда будут складываться итоговые файлы
    :return:
    """
    global path_to_end_folder
    path_to_end_folder = filedialog.askdirectory()

def select_file_docx():
    """
    Функция для выбора файла Word
    :return: Путь к файлу шаблона
    """
    global file_docx
    file_docx = filedialog.askopenfilename(
        filetypes=(('Word files', '*.docx'), ('all files', '*.*')))

def select_file_data_xlsx():
    """
    Функция для выбора файла с данными на основе которых будет генерироваться документ
    :return: Путь к файлу с данными
    """
    global file_data_xlsx
    # Получаем путь к файлу
    file_data_xlsx = filedialog.askopenfilename(filetypes=(('Excel files', '*.xlsx'), ('all files', '*.*')))

def processing_qr_code():
    """
    Фугкция для обработки данных
    :return:
    """
    checkbox = checkbox_type.get()

    try:
        df = pd.read_excel(file_data_xlsx)
        if checkbox == 0:
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
                    qr = qrcode.QRCode(box_size=2)  # создаем экземпляр класса
                    qr.add_data(qr_str)  # добавляем данные
                    # создаем картинку
                    img = qr.make_image(fill_color="black", back_color="white")
                    # меняем размер
                    img = img.resize((110, 110))
                    # очищаем от запрещенных символов
                    fio = re.sub(r'[<> :"?*|\\/]',' ',fio)
                    # проверяем наличие папки с названием группы, если ее нет то создаем и сохраняем файл
                    if os.path.isdir(f'{path_to_end_folder}/{group}'):
                        if os.path.isfile(f'{path_to_end_folder}/{group}/{fio}.png'):
                            # если такой файл есть то добавляем постфикс в виде индекса строки
                            img.save(f'{path_to_end_folder}/{group}/{fio}_{row[0]}.png')
                        else:
                            img.save(f'{path_to_end_folder}/{group}/{fio}.png')
                    else:
                        os.mkdir(f'{path_to_end_folder}/{group}')
                        img.save(f'{path_to_end_folder}/{group}/{fio}.png')
                    print(row)

        elif checkbox == 1:
            # перебираем список
            for row in df.itertuples():
                id_qr = row[1]  # получаем значение первой колонки по которой будут различаться колонки
                # создаем строку для qr кода
                qr_str = '\n'.join(row[1:])
                qr = qrcode.QRCode(box_size=2)  # создаем экземпляр класса
                qr.add_data(qr_str)  # добавляем данные
                # создаем картинку
                img = qr.make_image(fill_color="black", back_color="white")
                # меняем размер
                img = img.resize((110, 110))
                # очищаем от запрещенных символов
                id_qr = re.sub(r'[<> :"?*|\\/]', ' ', id_qr)
                # проверяем наличие такого файла
                if os.path.isfile(f'{path_to_end_folder}/{id_qr}.png'):
                    # если такой файл есть то добавляем постфикс в виде индекса строки
                    img.save(f'{path_to_end_folder}/{id_qr}_{row[0]}.png')
                else:
                    img.save(f'{path_to_end_folder}/{id_qr}.png')
                print(row)

    except NameError:
        messagebox.showerror('Ариадна ver 1.0',
                             f'Выберите файлы с данными и папку куда будет генерироваться файл')
    except KeyError as e:
        messagebox.showerror('Ариадна ver 1.0',
                             f'В таблице нет колонки {e.args}!\nПроверьте наличие колонки')
    except ValueError as e:
        messagebox.showerror('Ариадна ver 1.0',
                             f'В таблице нет колонки {e.args}!\nПроверьте написание названия колонки')
    except FileNotFoundError:
        messagebox.showerror('Ариадна ver 1.0',
                             f'Перенесите файлы которые вы хотите обработать в корень диска. Проблема может быть\n '
                             f'в слишком длинном пути к обрабатываемым файлам')
    else:
        messagebox.showinfo('Ариадна ver 1.0', 'Данные успешно обработаны')

if __name__ == '__main__':
    window = Tk()
    window.title('Ариадна ver 1.0')
    window.geometry('700x860')
    window.resizable(False, False)


    # Создаем объект вкладок

    tab_control = ttk.Notebook(window)

    # Создаем вкладку обработки данных для Приложения 6
    tab_qr_code = ttk.Frame(tab_control)
    tab_control.add(tab_qr_code, text='Создание QR кодов')
    tab_control.pack(expand=1, fill='both')
    # Добавляем виджеты на вкладку Создание образовательных программ
    # Создаем метку для описания назначения программы
    lbl_hello = Label(tab_qr_code,
                      text='Центр опережающей профессиональной подготовки Республики Бурятия\n'
                           'Программа для массовой генерации QR-кодов\n'
                           'по табличным данным')
    lbl_hello.grid(column=0, row=0, padx=10, pady=25)

    # Картинка
    path_to_img = resource_path('logo.png')

    img = PhotoImage(file=path_to_img)
    Label(tab_qr_code,
          image=img
          ).grid(column=1, row=0, padx=10, pady=25)

    # Создаем кнопку Выбрать файл с данными
    btn_choose_data = Button(tab_qr_code, text='1) Выберите файл с данными', font=('Arial Bold', 20),
                             command=select_file_data_xlsx
                             )
    btn_choose_data.grid(column=0, row=2, padx=10, pady=10)

    # Создаем кнопку для выбора папки куда будут генерироваться файлы

    btn_choose_end_folder = Button(tab_qr_code, text='2) Выберите конечную папку', font=('Arial Bold', 20),
                                   command=select_end_folder
                                   )
    btn_choose_end_folder.grid(column=0, row=3, padx=10, pady=10)

    # создаем переключатели

    checkbox_type = IntVar()

    # Создаем фрейм для размещения переключателей(pack и грид не используются в одном контейнере)
    frame_rb_type = LabelFrame(tab_qr_code, text='1) Выберите режим')
    frame_rb_type.grid(column=0, row=1, padx=10)
    #
    Radiobutton(frame_rb_type, text='А) Обработка стандартной таблицы', variable=checkbox_type,
                value=0).pack()
    Radiobutton(frame_rb_type, text='Б) Обработка произвольной таблицы', variable=checkbox_type,
                value=1).pack()

    #Создаем кнопку обработки данных

    btn_proccessing_qr = Button(tab_qr_code, text='3) Создать QR', font=('Arial Bold', 20),
                                  command=processing_qr_code
                                  )
    btn_proccessing_qr.grid(column=0, row=6, padx=10, pady=10)

    window.mainloop()