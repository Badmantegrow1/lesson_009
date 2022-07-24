# -*- coding: utf-8 -*-

# import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import time
import shutil


path_in = 'icons'
my_dir = os.path.dirname(__file__)
path_out = os.path.normpath(os.path.join(my_dir, 'icons_by_year'))
os.makedirs(path_out, exist_ok=True)


class FilesArrange:

    def __init__(self, folder_in, folder_out):
        self.folder_in = folder_in
        self.folder_out = folder_out
        self.extract()

    def extract(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_in):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                file_year = str(file_time[0])
                file_month = str(file_time[1])

                file_src_year = os.path.normpath(os.path.join(path_out, file_year))
                os.makedirs(file_src_year, exist_ok=True)

                file_src_year_month = os.path.normpath(os.path.join(file_src_year, file_month))
                os.makedirs(file_src_year_month, exist_ok=True)

                shutil.copy2(full_file_path, file_src_year_month)


FilesArrange(path_in, path_out)


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
