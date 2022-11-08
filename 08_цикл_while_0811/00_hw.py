a = []
length = int(input('Введите длину списка: '))

for i in range(length):  # повторить length раз
    n = int(input('Введи число: '))
    a.append(n)

print(a)
mult = 1
for i in range(len(a)):  # повторить <длина списка> раз
    mult *= a[i]
print(mult)
