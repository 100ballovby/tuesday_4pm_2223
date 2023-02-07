import json


def json_to_object(json_file):
    with open(json_file, 'r') as file:
        data = json.loads(file.read())
    return data


def object_to_json(obj, file):
    with open(file, "w") as file:
        file.write(json.dumps(obj, indent=4))


todos = json_to_object("todos.json")
users = json_to_object("users.json")

print(todos)
print(users)

tasks_users = {}
for todo in todos:
    if todo["completed"]:
        if todo["userId"] not in tasks_users:
            tasks_users[todo["userId"]] = {
                "completed": 1,
                "not_completed": 0
            }
        else:
            tasks_users[todo["userId"]]["completed"] += 1
    if not todo["completed"]:
        if todo["userId"] not in tasks_users:
            tasks_users[todo["userId"]] = {
                "completed": 0,
                "not_completed": 1
            }
        else:
            tasks_users[todo["userId"]]["not_completed"] += 1

print(tasks_users)
object_to_json(tasks_users, "todos_per_user.json")


usernames = {}
for u in users:
    usernames[u["id"]] = u["name"]

for user in tasks_users:
    print(f'User: {usernames[user]}.')
    print(f'Completed: {tasks_users[user]["completed"]} tasks;')
    print(f'Didn\'t completed: {tasks_users[user]["not_completed"]} tasks.')
    print()


