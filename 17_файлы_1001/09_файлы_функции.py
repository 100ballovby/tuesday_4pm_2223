def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)


write_file('file_with_function.txt', open('alice.txt').read())


