str1 = input('Введите строку: ')
str2 = input('Введите другую строку: ')

if len(str1) > len(str2):
    print(str1)
elif len(str1) < len(str2):
    print(str2)
else:
    print('Строки одинаковые.')
