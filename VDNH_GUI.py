"""
Графический интерфейс для функций подготовки данных к ВДНХ
"""

from create_svod_trudvsem_VDNH import vdnh_processing_data_trudvsem # генерация свода для куар
from create_qr_multi_sheet import processing_generate_data # генерация куар и джейсонов

import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

pd.options.mode.chained_assignment = None  # default='warn'
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller
    Функция чтобы логотип отображался"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


"""
Вспомогательные функции для обработки даннных с Работы в России
"""
def select_file_csv_trudvsem():
    """
    Функция для выбора файла csv
    """
    global file_csv_svod_trudvsem
    # Получаем путь к файлу
    file_csv_svod_trudvsem = filedialog.askopenfilename(filetypes=(('csv files', '*.csv'), ('all files', '*.*')))


def select_file_org_trudvsem():
    """
    Функция для выбора файла с организациями
    """
    global file_org_svod_trudvsem
    # Получаем путь к файлу
    file_org_svod_trudvsem = filedialog.askopenfilename(filetypes=(('Excel files', '*.xlsx'), ('all files', '*.*')))


def select_end_folder_svod_trudvsem():
    """
    Функия для выбора папки.Определенно вот это когда нибудь я перепишу на ООП
    :return:
    """
    global path_to_end_folder_svod_trudvsem
    path_to_end_folder_svod_trudvsem = filedialog.askdirectory()

"""
Функции для генерации куар
"""
def select_file_generate_data():
    """
    Функция для выбора файла с организациями
    """
    global file_generate_data
    # Получаем путь к файлу
    file_generate_data = filedialog.askopenfilename(filetypes=(('Excel files', '*.xlsx'), ('all files', '*.*')))


def select_end_folder_generate_data():
    """
    Функия для выбора папки.Определенно вот это когда нибудь я перепишу на ООП
    :return:
    """
    global path_to_end_folder_generate_data
    path_to_end_folder_generate_data = filedialog.askdirectory()




"""
Создание свода Работа в России
"""

def processing_svod_trudvsem_vdnh():
    """
    Функция для обработки данных с сайта Работа в России
    :return:
    """
    try:
        name_folder_column = str(entry_folder_column.get()) # Получаем название региона
        vdnh_processing_data_trudvsem(file_generate_data, path_to_end_folder_generate_data,)

    except NameError:
        messagebox.showerror('Кассандра Подсчет данных по трудоустройству выпускников',
                             f'Выберите файлы с данными и папку куда будет генерироваться файл')


"""
Создание QR
"""
def processing_generate_data_vdnh():
    """
    Функция для обработки данных с сайта Работа в России
    :return:
    """
    try:
        name_region = str(entry_region.get()) # Получаем название региона

        processing_generate_data(file_csv_svod_trudvsem, file_org_svod_trudvsem,path_to_end_folder_svod_trudvsem,name_region)

    except NameError:
        messagebox.showerror('Кассандра Подсчет данных по трудоустройству выпускников',
                             f'Выберите файлы с данными и папку куда будет генерироваться файл')


def on_scroll(*args):
    canvas.yview(*args)

def set_window_size(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Устанавливаем размер окна в 80% от ширины и высоты экрана
    if screen_width >= 3840:
        width = int(screen_width * 0.2)
    elif screen_width >= 2560:
        width = int(screen_width * 0.31)
    elif screen_width >= 1920:
        width = int(screen_width * 0.41)
    elif screen_width >= 1600:
        width = int(screen_width * 0.5)
    elif screen_width >= 1280:
        width = int(screen_width * 0.62)
    elif screen_width >= 1024:
        width = int(screen_width * 0.77)
    else:
        width = int(screen_width * 1)

    height = int(screen_height * 0.6)

    # Рассчитываем координаты для центрирования окна
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Устанавливаем размер и положение окна
    window.geometry(f"{width}x{height}+{x}+{y}")

def make_textmenu(root):
    """
    Функции для контекстного меню( вырезать,копировать,вставить)
    взято отсюда https://gist.github.com/angeloped/91fb1bb00f1d9e0cd7a55307a801995f
    """
    # эта штука делает меню
    global the_menu
    the_menu = Menu(root, tearoff=0)
    the_menu.add_command(label="Вырезать")
    the_menu.add_command(label="Копировать")
    the_menu.add_command(label="Вставить")
    the_menu.add_separator()
    the_menu.add_command(label="Выбрать все")


def callback_select_all(event):
    """
    Функции для контекстного меню( вырезать,копировать,вставить)
    взято отсюда https://gist.github.com/angeloped/91fb1bb00f1d9e0cd7a55307a801995f
    """
    # select text after 50ms
    window.after(50, lambda: event.widget.select_range(0, 'end'))


def show_textmenu(event):
    """
    Функции для контекстного меню( вырезать,копировать,вставить)
    взято отсюда https://gist.github.com/angeloped/91fb1bb00f1d9e0cd7a55307a801995f
    """
    e_widget = event.widget
    the_menu.entryconfigure("Вырезать", command=lambda: e_widget.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Копировать", command=lambda: e_widget.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Вставить", command=lambda: e_widget.event_generate("<<Paste>>"))
    the_menu.entryconfigure("Выбрать все", command=lambda: e_widget.select_range(0, 'end'))
    the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)


if __name__ == '__main__':
    window = Tk()
    window.title('Подготовка данных к ВДНХ ver 1.0')
    # Устанавливаем размер и положение окна
    set_window_size(window)
    window.resizable(True, True)
    # Добавляем контекстное меню в поля ввода
    make_textmenu(window)
    # Создаем вертикальный скроллбар
    scrollbar = Scrollbar(window, orient="vertical")

    # Создаем холст
    canvas = Canvas(window, yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)

    # Привязываем скроллбар к холсту
    scrollbar.config(command=canvas.yview)

    # Создаем ноутбук (вкладки)
    tab_control = ttk.Notebook(canvas)

    """
    Вкладка для создания свода из данных с сайта Работа в России
    """
    tab_svod_trudvsem = ttk.Frame(tab_control)
    tab_control.add(tab_svod_trudvsem, text='Свод Работа в России')

    svod_trudvsem_frame_description = LabelFrame(tab_svod_trudvsem)
    svod_trudvsem_frame_description.pack()

    lbl_hello_svod_trudvsem = Label(svod_trudvsem_frame_description,
                                    text='Центр опережающей профессиональной подготовки Республики Бурятия\n'
                                         'Аналитика по кадровой ситуации в регионе на основании данных \n'
                                         'с сайта Работа в России (trudvsem.ru) https://trudvsem.ru/opendata/datasets',
                                    width=60)
    lbl_hello_svod_trudvsem.pack(side=LEFT, anchor=N, ipadx=25, ipady=10)

    # Картинка
    path_to_img_svod_trudvsem = resource_path('logo.png')
    img_svod_trudvsem = PhotoImage(file=path_to_img_svod_trudvsem)
    Label(svod_trudvsem_frame_description,
          image=img_svod_trudvsem, padx=10, pady=10
          ).pack(side=LEFT, anchor=E, ipadx=5, ipady=5)

    # Создаем область для того чтобы поместить туда подготовительные кнопки(выбрать файл,выбрать папку и т.п.)
    frame_data_svod_trudvsem = LabelFrame(tab_svod_trudvsem, text='Подготовка')
    frame_data_svod_trudvsem.pack(padx=10, pady=10)

    # Кнопка для выбора файла csv
    btn_choose_data_svod_trudvsem = Button(frame_data_svod_trudvsem, text='1) Выберите файл скачанный с сайта\n'
                                                                          'Работа в России в формате csv',
                                           font=('Arial Bold', 15),
                                           command=select_file_csv_trudvsem
                                           )
    btn_choose_data_svod_trudvsem.pack(padx=10, pady=10)

    # Создаем кнопку для выбора файла с работодателями

    btn_choose_data_org_svod_trudvsem = Button(frame_data_svod_trudvsem, text='2) Выберите файл с работодателями',
                                                 font=('Arial Bold', 15),
                                                 command=select_file_org_trudvsem
                                                 )
    btn_choose_data_org_svod_trudvsem.pack(padx=10, pady=10)
    #
    # Создаем поле для ввода региона

    # Определяем текстовую переменную
    entry_region = StringVar()
    # Описание поля
    label_svod_trudvsem = Label(frame_data_svod_trudvsem,
                                             text='3) Введите название региона')
    label_svod_trudvsem.pack(padx=10, pady=10)
    # поле ввода имени листа
    svod_trudvsem_entry = Entry(frame_data_svod_trudvsem, textvariable=entry_region,
                                             width=30)
    svod_trudvsem_entry.pack(padx=10, pady=10)

    # Кнопка для выбора конечной папки
    btn_choose_end_folder_svod_trudvsem = Button(frame_data_svod_trudvsem, text='4) Выберите конечную папку',
                                                 font=('Arial Bold', 15),
                                                 command=select_end_folder_svod_trudvsem
                                                 )
    btn_choose_end_folder_svod_trudvsem.pack(padx=10, pady=10)



    btn_proccessing_data_svod_trudvsem = Button(tab_svod_trudvsem, text='5) Обработать данные',
                                                font=('Arial Bold', 20),
                                                command=processing_svod_trudvsem_vdnh
                                                )
    btn_proccessing_data_svod_trudvsem.pack(padx=10, pady=10)


    """
    Вкладка для qr  и джейсонов
    """
    tab_generate_data = ttk.Frame(tab_control)
    tab_control.add(tab_generate_data, text='Генерация QR и JSON')

    generate_data_frame_description = LabelFrame(tab_generate_data)
    generate_data_frame_description.pack()

    lbl_hello_generate_data = Label(generate_data_frame_description,
                                    text='Центр опережающей профессиональной подготовки Республики Бурятия\n'
                                         'Генерация QR и JSON \n'
                                         'с сайта Работа в России (trudvsem.ru) https://trudvsem.ru/opendata/datasets',
                                    width=60)
    lbl_hello_generate_data.pack(side=LEFT, anchor=N, ipadx=25, ipady=10)

    # Картинка
    path_to_img_generate_data = resource_path('logo.png')
    img_generate_data = PhotoImage(file=path_to_img_generate_data)
    Label(generate_data_frame_description,
          image=img_generate_data, padx=10, pady=10
          ).pack(side=LEFT, anchor=E, ipadx=5, ipady=5)

    # Создаем область для того чтобы поместить туда подготовительные кнопки(выбрать файл,выбрать папку и т.п.)
    frame_data_generate_data = LabelFrame(tab_generate_data, text='Подготовка')
    frame_data_generate_data.pack(padx=10, pady=10)

    # Кнопка для выбора файла csv
    btn_choose_data_generate_data = Button(frame_data_generate_data, text='1) Выберите файл скачанный с сайта\n'
                                                                          'Работа в России в формате csv',
                                           font=('Arial Bold', 15),
                                           command=select_file_csv_trudvsem
                                           )
    btn_choose_data_generate_data.pack(padx=10, pady=10)

    # Создаем кнопку для выбора файла с работодателями

    btn_choose_data_org_generate_data = Button(frame_data_generate_data, text='2) Выберите файл с работодателями',
                                               font=('Arial Bold', 15),
                                               command=select_file_org_trudvsem
                                               )
    btn_choose_data_org_generate_data.pack(padx=10, pady=10)
    #
    # Создаем поле для ввода колонки по которой будут

    # Определяем текстовую переменную
    entry_region = StringVar()
    # Описание поля
    label_generate_data = Label(frame_data_generate_data,
                                text='3) Введите название региона')
    label_generate_data.pack(padx=10, pady=10)
    # поле ввода имени листа
    generate_data_entry = Entry(frame_data_generate_data, textvariable=entry_region,
                                width=30)
    generate_data_entry.pack(padx=10, pady=10)

    # Кнопка для выбора конечной папки
    btn_choose_end_folder_generate_data = Button(frame_data_generate_data, text='4) Выберите конечную папку',
                                                 font=('Arial Bold', 15),
                                                 command=select_end_folder_generate_data
                                                 )
    btn_choose_end_folder_generate_data.pack(padx=10, pady=10)

    btn_proccessing_data_generate_data = Button(tab_generate_data, text='5) Обработать данные',
                                                font=('Arial Bold', 20),
                                                command=processing_generate_data_vdnh
                                                )
    btn_proccessing_data_generate_data.pack(padx=10, pady=10)






    # Создаем виджет для управления полосой прокрутки
    canvas.create_window((0, 0), window=tab_control, anchor="nw")

    # Конфигурируем холст для обработки скроллинга
    canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))
    scrollbar.pack(side="right", fill="y")

    # Вешаем событие скроллинга
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    window.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_textmenu)
    window.bind_class("Entry", "<Control-a>", callback_select_all)
    window.mainloop()