def create_list(p=1):
    persons = []
    for prs in range(p):
        person = {
            "name": "",
            "age": "",
            "department": "",
            "city": "",
        }
        for key in person:
            data = input(f'{key}: ')
            person[key] = data
        persons.append(person)
    return persons


employees = create_list(3)
print(employees)

