tab_generate_data = ttk.Frame(tab_control)
tab_control.add(tab_generate_data, text='Генерация QR и JSON')

generate_data_frame_description = LabelFrame(tab_generate_data)
generate_data_frame_description.pack()

lbl_hello_generate_data = Label(generate_data_frame_description,
                                text='Центр опережающей профессиональной подготовки Республики Бурятия\n'
                                     'Аналитика по кадровой ситуации в регионе на основании данных \n'
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
# Создаем поле для ввода региона

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