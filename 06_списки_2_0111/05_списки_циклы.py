squares = []
# наполнить список квадратами чисел от 1 до 15
for i in range(1, 16):
    # добавлять числа в список
    squares.append(i ** 2)
print(squares)
# посчитать среднее арифметическое
summ = 0
for element in squares:  # список как последовательность для цикла
    summ += element  # складываю каждое число в списке с переменной summ
print('Среднее арифметическое: ', summ / len(squares))


