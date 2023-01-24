import json

data = {
    'employees' : [
        {
            'name' : 'John Doe',
            'department' : 'Marketing',
            'place' : 'Remote'
        },  # индекс 0
        {
            'name' : 'Jane Doe',
            'department' : 'Software Engineering',
            'place' : 'Remote'
        },  # индекс 1
        {
            'name' : 'Don Joe',
            'department' : 'Software Engineering',
            'place' : 'Office'
        }  # индекс 2
    ]
}

"""Для записи в JSON-файлы используются два метода:
- dump() - превращает словарь в поток JSON для записи в файл или сокет 
- dumps() - превращает словарь в строку JSON 
"""
json_string = json.dumps(data["employees"], indent=4)  # превратить в JSON-строку список из ключа employees
# indent=4 - делает красивые отступы для каждой строки JSON-файла

# запись словаря в файл
with open("employees.json", "w") as file:
    file.write(json_string)

# чтение файла JSON
with open("employees.json", 'r') as json_file:
    dict = json.load(json_file)
    print(dict)
    print(type(dict))

