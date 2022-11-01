n = int(input('Введи число: '))
a = int(input('Введи конец таблицы умножения '))

for i in range(1, a + 1):
    print(n, '*', i, '=', i * n)

