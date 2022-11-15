n = int(input('Введите число: '))
count = 0  # количество введенных
summ = 0

while n != 0:  # повторять, пока не введут 0
    summ += n
    count += 1
    n = int(input('Введите число: '))

print('сумма: ', summ)
print('Среднее: ', summ / count)

