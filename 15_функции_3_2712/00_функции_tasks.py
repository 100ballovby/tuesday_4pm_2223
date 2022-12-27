def search_symbol(string, symbol):
    index = -1
    for i in range(len(string)):
        if symbol == string[i]:
            index = i
            break
    return index


def count_symbols(string):
    count_one = 0
    res = 0
    for i in range(len(string)):
        if string[i] == '1':
            count_one += 1
        elif string[i] == '0':
            if count_one % 2 != 0 and count_one > 1:
                res += count_one
            count_one = 0
    return res

n = '100111010101111101'
print(count_symbols(n))

