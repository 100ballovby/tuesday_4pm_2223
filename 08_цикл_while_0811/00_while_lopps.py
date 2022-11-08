name = input('Как тебя зовут?')

while not name[0].isupper():
    print('Напиши с большой буквы!')
    name = input('Как тебя зовут?')

print('Спасибо!')
