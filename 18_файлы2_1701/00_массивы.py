import random as r


def create_array(size, start, stop):
    arr = []
    for i in range(size):
        arr.append(r.randint(start, stop))
    return arr


def array_to_file(path, arr, size):
    columns = round(size / 10)
    i = 1
    with open(path, 'w') as file:
        while (i < size):
            if i % columns == 0:
                file.write(str(arr[i-1]) + '\n')
            else:
                file.write(str(arr[i-1]) + ' ')
            i += 1


def find_max_in_file(path):
    with open(path) as file:
        data = file.readlines()  # список со всеми строками из файла
        max = 0
        for line in data:  # просматриваю каждую строку из файла
            lst = line.strip().split(' ')  # превращаю строку из файла в список и убираю лишние символы
            for num in lst:  # перебираю каждое значение из строки
                if eval(num) > max:  # сравниваю преобрзованное значение из строки с max
                    max = eval(num)  # если значение больше max, сохраняю его как максимальное
    return max



array = create_array(40, -100, 100)
print(array)
array_to_file('sample.txt', array, 40)
print(find_max_in_file('sample.txt'))