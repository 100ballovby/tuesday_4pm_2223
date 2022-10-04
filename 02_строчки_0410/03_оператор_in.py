phrase = input('Введите что-то: ')
symbol = input('Введи символ: ')

print('Символ в строке: ', symbol in phrase)  # проверяю наличие символа в строке
print('Индекс символа: ', phrase.index(symbol))  # нахожу индекс символа в строке


