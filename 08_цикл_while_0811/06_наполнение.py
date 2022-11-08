import random as r
matrix = []
n = 3  # строки матрицы
m = 3  # количество элементов в строке

for i in range(n):  # по количеству линий
    line = []  # создать линию (пустой список)
    for j in range(m):  # наполнить линию элементами в количеству m
        line.append(r.randint(1, 100))  # добавить число в линию
    matrix.append(line)  # линию с элементами добавить в матрицу

print(matrix)
