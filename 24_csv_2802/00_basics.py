import csv
from _csv import reader


def read_csv(filename):
    with open(filename, 'r') as csv_file:
        # reader будет читать csv файл, значения в котором разделены ,
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0  # счетчик строк в файле
        for line in csv_reader:  # reader формирует список из значений
            if line_count == 0:  # если мы смотрим первую строчку
                print(f'Заголовки таблицы: {", ".join(line)}')
                line_count += 1  # увеличиваю счетчик на единицу
            else:
                print(f'\t{line[0]} работает в отделе {line[1]}, месяц рождения {line[2]}.')
                line_count += 1
        print(f'Обработано {line_count} строк.')


def append_csv(filename, el_list):
    """
    Добавляет строки в сsv-файл.
    param: filename - имя файла для записи
    param: el_list - двумерный список строк, содержащий в себе элементы
    return: None
    """
    with open(filename, 'a') as csv_file:  # режим a позволяет дополнить файл без перезаписывания
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)  # writer пишет в файл значения
        # quotechar - это символ, которым закрываем поля
        # QUOTE_MINIMAL - в кавычки будут заключены те поля, которые содержат delimeter или quotechar
        for line in el_list:
            csv_writer.writerow(line)  # записывает строки в файл


def csv_to_matrix(filename):
    """
    Функция читает CSV-файл и записывает строки и элементы из него
    в двумерный список, который затем возвращается из функции.
    param: filename - имя файла для чтения
    return: double list
    """
    res = []
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for i in reader:
            line = []
            for j in range(len(i)):
                line.append(i[j])
            res.append(line)
    return res



read_csv('employees.csv')
peoples = [
    ['John Smith', 'Accounting', 'November'],
    ['Erica Meyers', 'IT, System', 'January'],
    ['Fill Lebovski', 'Marketing, Logistic', 'June',],
]
"""
Все строки в CSV-файле фактически представляют собой списки.
Сам файл - это подобие двумерного списка, так как объект reader 
возвращает список, содержаший в себе элементы.
"""
#append_csv("employees.csv", peoples)  <- эта функция записывает в таблицу все значения из списка peoples
employees = csv_to_matrix('employees.csv')
print(employees)
