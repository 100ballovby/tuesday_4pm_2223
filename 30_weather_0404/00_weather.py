import os
import requests as r
from datetime import datetime

cities = ['Минск', 'Санкт-Петербург', 'Берлин',
           'Рим', 'Токио', 'Урюпинск', 'Пекин']


def get_forecast(city):
    token = os.environ.get('API_KEY')  # сохранил значение ключа из переменной среды в обычную переменную
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': token,
        'lang': 'ru',
        'units': 'metric',
        'q': city
    }

    response = r.get(url, params=params).json()
    return response


for city in cities:
    forecast = get_forecast(city)
    try:
        date = datetime.fromtimestamp(forecast["dt"])
        print(f'Город: {city}')
        print(f'Температура: {forecast["main"]["temp"]}, ощущается как {forecast["main"]["feels_like"]}')
        print(f'Сейчас {forecast["weather"][0]["description"]}')
        print(f'Дата: {date.strftime("%d.%m.%Y, %H:%M")}')
        print(f'Координаты: {forecast["coord"]["lat"]},{forecast["coord"]["lon"]}\n')
    except KeyError:
        print(f'Город: {city} не найден!')
