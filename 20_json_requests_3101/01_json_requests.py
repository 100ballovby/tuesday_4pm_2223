import json
import requests as req  # pip install requests (в терминале)

def make_request(url):
    response = req.get(url)  # отсылаю GET-запрос к адресу URL
    return response.text


url = "https://jsonplaceholder.typicode.com/todos"  # сохраняем URL-адрес, по которому будем подключаться
resp = make_request(url)
print(resp)
