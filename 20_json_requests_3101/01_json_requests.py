import json
import requests as req  # pip install requests (в терминале)

def make_request(url):
    response = req.get(url)  # отсылаю GET-запрос к адресу URL
    response_json = response.json()
    return response_json


url = "https://jsonplaceholder.typicode.com/todos"  # сохраняем URL-адрес, по которому будем подключаться
resp = make_request(url)  # здесь получаю сразу объект Python

url_2 = "https://jsonplaceholder.typicode.com/users"
resp_2 = make_request(url_2)   # получаем пользователей

with open("todos.json", "w") as json_file:
    json_file.write(json.dumps(resp, indent=4))

with open("users.json", "w") as json_file:
    json_file.write(json.dumps(resp_2, indent=4))


count_uncompleted = 0
for task in resp:
    if not task["completed"]:  # если в ключе completed False
        print(task["id"])  # вывести значение ключа id
        count_uncompleted += 1  # увеличить счетчик
print(f"Not completed tasks: {count_uncompleted}")

users_tasks = {}
for task in resp:
    if task["completed"]:  # если задача имеет статус "выполнено"
        if task["userId"] not in users_tasks:  # если пользователь с таким ID не обнаружен в словаре
            users_tasks[task["userId"]] = 1  # добавить его ID как ключ и поставить значение выполненных задач 1
        else:  # если пользователь с таким ID есть в словаре
            users_tasks[task["userId"]] += 1  # добавляем этому пользователю +1 выполненную задачу

print(users_tasks)

users = {}
for user in resp_2:  # перебираем юзеров
    users[user["id"]] = user["name"]

print(users)
