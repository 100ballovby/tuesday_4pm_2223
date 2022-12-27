def summary(*args):
    res = 0
    for i in range(len(args)):
        res += args[i]
    return res


def mult(*args):
    res = 1
    for i in range(len(args)):
        res *= args[i]
    return res


print(summary(5, 4))
print(summary(2, 4, 6, 7, 1, 8))
print(summary(8, 1, 2, 9, 12, 3, 4, 5, 12, 67, 89, 100))
print(summary(1))


