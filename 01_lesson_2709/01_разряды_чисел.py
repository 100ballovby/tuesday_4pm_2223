num = int(input('Введи число: '))

tens = num // 10  # нахожу целую часть от деления
units = num % 10  # нахожу остаток от деления

print(num, '=', tens, 'и', units)
print(tens + units)

num_1 = int(input('Введи трехзначное число: '))

hundreds = num_1 // 100
tens = num_1 % 100 // 10  # нахожу целую часть от деления
units = num_1 % 10  # нахожу остаток от деления

print(num_1, '=', hundreds, 'и', tens, 'и', units)
print(hundreds + tens + units)
