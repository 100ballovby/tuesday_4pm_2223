import requests as r
import json


def get_rates(currency):
    url = 'https://api.coinbase.com/v2/exchange-rates'
    params = {'currency': currency}
    response = r.get(url, params=params).json()  # подключиться к URL
    """params (до равно) - это параметр функции get(), а 
    params (после равно) - это то, что мы хотим передать,
    но называть переменную после равно можно любым словом"""
    return response  # возвращаю ответ сервера в формате JSON

def get_currencies():
    url = 'https://api.coinbase.com/v2/currencies'
    response = r.get(url).json()  # подключиться к URL
    return response  # возвращаю ответ сервера в формате JSON

cur = input('Введите название валюты: ').upper()
rates = get_rates(cur)  # когда нам введут валюту, мы подставим ее в функцию

with open(f'rates_{cur}.json', 'w') as file:
    file.write(json.dumps(rates, indent=4))

currencies = get_currencies()  # сохраняем словарь с валютами в переменной
c_names = {}
for i in range(len(currencies['data'])):
    c_names[currencies['data'][i]['id']] = currencies['data'][i]['name']

data = rates['data']['rates']
for rate in data:
    try:  # попытаться вывести
        print(f'1 {cur} is {data[rate]} {c_names[rate]}')
    except KeyError:  # если возникла ошибка ключа
        pass  # ничего не делать







