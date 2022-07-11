# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


def print_txt():
    print('+---------+----------+')
    print('|  буква  | частота  |')
    print('+---------+----------+')


class Static:

    def __init__(self, file_name):
        self.file_name = file_name
        self.sum = None
        self.sorted_tuple = None
        self.stat = {}

    def unzip(self):
        z_file = zipfile.ZipFile(self.file_name, 'r')
        for filename in z_file.namelist():
            z_file.extract(filename)

    def open_file(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.sorted_char(line)

    def sorted_char(self, line):
        for ch in line:
            if ch in self.stat:
                self.stat[ch] += 1
            else:
                if ch.isalpha():
                    self.stat[ch] = 1

    def sorted_tup(self):
        print_txt()
        self.sum = 0
        self.sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=False)
        for key, value in self.sorted_tuple:
            if len(str(value)) == 1:
                space = '     '
            elif len(str(value)) == 2:
                space = '    '
            elif len(str(value)) == 3:
                space = '   '
            elif len(str(value)) == 4:
                space = '  '
            elif len(str(value)) == 5:
                space = ' '
            else:
                space = ''
            print('|    {}    |   {}{} |'.format(key, value, space))
            self.sum += value
        self.print_sum()

    def print_sum(self):
        print('+---------+----------+')
        print('|  итого  | {}  |'.format(self.sum))
        print('+---------+----------+')


static = Static(file_name='python_snippets/voyna-i-mir.txt')
static.open_file()
static.sorted_tup()

#  После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
