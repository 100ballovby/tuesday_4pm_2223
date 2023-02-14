import requests as r
import json


url = "https://api.thedogapi.com/v1/breeds"  # адрес сайта, к которому будем поодклбючаться
ans = r.get(url)  # подключаюсь к сайту

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=4))


def read_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())

write_file("dogs_breeds.json", ans.json())
user = read_file("user.json")  # читаю файл и сохраняю его содержимое
print(user)


