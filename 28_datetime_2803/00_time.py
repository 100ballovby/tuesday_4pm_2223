import time
import sys

sys.set_int_max_str_digits(0)

print(time.time())


def calcProd():
    # вычисление произведения первых 100000 чисел
    prod = 1
    for i in range(1, 100001):
        prod *= i
    return prod


start = time.time()  # фиксирую точку начала работы программы
res = calcProd()  # считаю произведение 100000 чисел
end = time.time()  # фиксирую точку окончания работы программы
print(f'Длина числа: {len(str(res))}')
print(f'Время работы программы: {end - start}')




