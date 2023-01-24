d = {
    "name": "John",
    "surname": "Doe",
    "age": 35,
    "city": "Washington",
}

for key in d.keys():  # перебрать каждый ключ из словаря d
    print(f'Ключ: {key}')  # вывести каждый ключ

for value in d.values():  # перебрать каждое значение в словаре d
    print(f'Значение: {value}')  # вывести каждое значение из словаря

for key, value in d.items():  # перебрать одновременно и ключи, и значения в словаре d
    print(f'Ключ: "{key}", значение: "{value}";')
