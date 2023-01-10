path = "pi_million_digits.txt"  # сохранили путь к файлу
with open(path) as file:
    pi_string = ''  # здесь храним число π
    for line in file.readlines():  # создает список из строк файла
        pi_string += line.strip()  # убираем пробелы и переносы строк

print(pi_string)
print(len(pi_string))
birth = input('Введите дату рождения ддммгг')
if birth in pi_string:
    print('Ваша дата рождения есть в числе π')
else:
    print('Вашей даты рождения нет в числе π')
