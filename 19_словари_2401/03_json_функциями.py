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

def dict_to_json(obj, filename):
    """Функция принимает словарь и имя файла
    и записывает содержимое словаря в файл JSON"""
    json_string = json.dumps(obj, indent=4)
    with open(f"{filename}.json", "w") as file:
        file.write(json_string)


def json_to_dict(file):
    with open(file, 'r') as json_file:
        dict = json.load(json_file)
    return dict


dict_to_json(data, "employees")
res = json_to_dict("employees.json")
print(res)
