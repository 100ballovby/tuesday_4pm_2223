"""
Обрезать строку до определенного символа.
"""


def slice_before(string, symbol):
    index = -1
    for i in range(len(string)):
        if string[i] == symbol:  # сравниваем индексы строки с тем, что передали
            index = i  # и сохраняем индекс первого найденного
            break
    if index >= len(string):
        return string
    else:
        return string[:index]

print(slice_before('hello-world', '-'))



