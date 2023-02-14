import json


def read_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


dogs = read_file("dogs_breeds.json")
for dog in dogs:
    print(f'{dog["name"]}\t |\t {dog["image"]["url"]}\t |\t {dog["life_span"]}')


# выведем породы и страны, в которых они были выведены
in_usa = 0
for breed in dogs:
    try:
        print(f'{breed["name"]} was bred in {breed["country_code"]}')
        if breed["country_code"] == "US":
            in_usa += 1
    except KeyError:  # если поймали ошибку "Нет ключа"
        pass  # ничего не делать
print(f"{in_usa} dogs was bred in the USA.")

