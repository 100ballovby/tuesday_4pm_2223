import csv

""" чтобы получить названия столбцов таблицы,
будем использовать особый класс DictReader. 
он позволяет превратить таблицу в подобие словаря 
и затем при помощи параметра fieldnames получить 
список заголовков таблицы """
with open('employees.csv', 'r') as file:
    f = file.readlines()  # возврващает список из строк файла
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
    print(headers)


