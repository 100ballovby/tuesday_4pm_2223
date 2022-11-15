n = int(input('Введите число: '))

ld = 2  # наименьший делитель
while ld < n:
    if n % ld == 0:
        print(ld)
        break
    ld += 1
