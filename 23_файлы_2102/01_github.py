import requests as r
import json


url = 'https://api.github.com/search/repositories'
query = {'q': 'requests'}  # параметры запроса к серверу (вставляются через ?q=)
response = r.get(url, params=query)
print(response.url)  # печатаю url обращения к серверу
js = response.json()  # превращаю ответ сервера в JSON
for repo in js['items']:  # перебираю элементы ответа
    print(repo["svn_url"], repo["name"])
