def length(iterable):
    """Функция-аналог встроенной len()
    :param iterable: итерабельный объект
    :return длина объекта"""
    count = 0
    for i in iterable:  # перебираю каждый элемент iterable
        count += 1
    return count


a = 'kjfhjkq3e320'
b = [5, 2, 1, 7, 3, 10]
print(length(a))
print(length(b))
# print(length(5)) <- число нельзя поместить в цикл, поэтому возникнет TypeError



