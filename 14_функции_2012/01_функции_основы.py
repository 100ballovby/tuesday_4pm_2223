from logic import *

symbol = input('Введите действие: ')
n1 = input('Число 1: ')
n2 = input('Число 2: ')

try:
    n1 = eval(n1)
    n2 = eval(n2)
except NameError:
    print('Это не число!')

if symbol == '+':
    res = add(n1, n2)
    print(res)
elif symbol == '-':
    res = subtract(n1, n2)
    print(res)
elif symbol == '*':
    res = multiply(n1, n2)
    print(res)
elif symbol == '/':
    res = division(n1, n2)
    print(res)
else:
    print('Недопустимое действие!')
