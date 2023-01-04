word = 'закаdjfhз'


def check_palin(string):
    is_palindrome = True
    for i in range(len(string)):
        if string[i] != string[len(string) - 1 - i]:
            is_palindrome = False
            break  # если буквы не совпали, дальше искать смысла нет
    return is_palindrome


def check_palin2(string):
    return string[::] == string[::-1]  # можно сделать ТОЛЬКО в Python

print(f'{word} is palindrome: {check_palin(word)}')
word = "анна"
print(f'{word} is palindrome: {check_palin2(word)}')


