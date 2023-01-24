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
print(data["employees"][0]["department"])
# словарь_data[ключ employees][первый_элемент_списка][ключ department]
for i in range(len(data["employees"])):
    person = data["employees"][i]
    for key in person.keys():
        print(f"{key}: {person[key]}")
    print()