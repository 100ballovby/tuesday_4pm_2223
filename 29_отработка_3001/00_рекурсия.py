import random as r
import sys

sys.setrecursionlimit(10000)  # установить количество повторений рекурсии в количестве 10000 штук

def calcSumNums(A):
    # базовый случай - это случай выхода из функции с прекращением ее работы
    if A == []:  # если список опустел
        return 0
    # рекурсивный случай - это ситуация, в которой функция начинает выполнять повторения (если список не пустой)
    else:
        summ = calcSumNums(A[1:])  # сохраняю остаток списка
        summ += A[0]  # добавляю первый элемент к переменной
        return summ


def calcNegative(A):  # итератор в рекурсии есть - это она сама
    # вычислить количество отрицательных чисел
    if A == []:
        return 0
    else:
        count = calcNegative(A[1:])
        if A[0] < 0:
            count += 1
        return count


def power(n, exp):
    if exp > 0:  # рекурсивный случай
        return n * power(n, exp - 1)
    else:
        return 1


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def summ(n):
    if n == 1:
        return 1
    else:
        return n + summ(n - 1)


def printLeadingDigit(n):
    if n < 10:  # если число меньше 10 (оно является цифрой)
        return n
    else:
        return printLeadingDigit(n // 10)


def countDigits(n):
    if n < 10:  # если число меньше 10 (оно является цифрой)
        return 1
    else:
        return 1 + countDigits(n // 10)


def count_solutions(n, x=1, y=1):
    if x ** 2 + y ** 2 >= n:
        return 0
    else:
        count = 1
        count += count_solutions(n, x+1, y)
        if x != y:
            count += count_solutions(n, x, y+1)
        return count


print(f'посчитать сумму списика [5, 4, 2, 1]: {calcSumNums([5, 4, 2, 1])}')
print(f'количество отрицательных чисел [-2, -6, 2, 1, -9, 8, 0, 3]:  {calcNegative([-2, -6, 2, 1, -9, 8, 0, 3])}')
print(f'2^3 = {power(2, -3)}')
n = r.randint(0, 15)
print(f'{n}! = {factorial(n)}')
#print(f'сумма от 1 до {n} = {summ(n)}')
num = r.randint(100, 100000)
print(f'Старшая цифра числа {num} - {printLeadingDigit(num)}')
print(f'Количество цифр числа {num} - {countDigits(num)}')
print(f'количество натуральных решений для n = {n}: {count_solutions(n)}')

"""
Напишите программу, которая печатает десятеричная (число, записанное цифрами от 0 до 9)
запись введенного натурального числа,
использующую только операции печати цифр от 0 до 9
"""

