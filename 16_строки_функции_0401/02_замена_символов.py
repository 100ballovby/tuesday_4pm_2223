def first_three(string):
    if len(string) <= 3:
        return string
    else:
        return string[:3]  # срез строки с 0 индекса ДО 3 -> 0,1,2

print(first_three('мама мыла раму'))
print(first_three('try'))
