path = "pi_digits.txt"  # сохранили путь к файлу
with open(path) as file:
    pi_string = ''  # здесь храним число π
    for line in file.readlines():  # создает список из строк файла
        pi_string += line.strip()  # убираем пробелы и переносы строк

print(pi_string)
