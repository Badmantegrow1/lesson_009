# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Logs:

    def __init__(self, file_name):
        self.file = None
        self.date = None
        self.lines = None
        self.count_nok = None
        self.file_content = None
        self.file_name_logs = None
        self.file_name = file_name

    def open_and_clear_file(self):
        self.file = open(self.file_name, mode='w+')
        self.file_content = self.file.read()
        self.file.write('')
        self.file.close()

    def open_and_write_file(self):
        self.file_name = 'out1.txt'
        self.file = open(self.file_name, mode='a')
        self.file_content = f'{self.date} {self.count_nok}\n'
        self.file.write(self.file_content)
        self.file.close()

    def file_read(self):
        self.file_name_logs = 'events.txt'
        self.count_nok = 0
        self.date = []
        self.open_file_and_sorted()

    def open_file_and_sorted(self):
        with open(self.file_name_logs, 'r', encoding='cp1251') as file:
            file_contents = file.readlines()
            file_contents.sort(key=lambda line: (line.split(' ')[0]), reverse=False)
            self.append_in_list(file_contents)

    def append_in_list(self, file_contents):
        for line in file_contents:
            if 'NOK' not in line:
                continue
            elif line[1:17] in self.date:
                self.count_nok += 1
            elif line[1:17] not in self.date:
                self.write_file(line)

    def write_file(self, line):
        if self.count_nok > 0:
            self.open_and_write_file()
            self.count_reload()
            self.date[0] = (line[1:17])
        else:
            self.count_reload()
            self.date.append(line[1:17])

    def count_reload(self):
        self.count_nok = 0
        self.count_nok += 1

    def write_file_close(self):
        self.open_and_write_file()


logs = Logs(file_name='out1.txt')
logs.open_and_clear_file()
logs.file_read()
logs.write_file_close()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
