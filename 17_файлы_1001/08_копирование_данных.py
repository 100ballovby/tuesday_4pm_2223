path1 = 'alice.txt'
path2 = 'alice copy.txt'

with open(path1) as read_file:
    lines = read_file.readlines()
    with open(path2, 'w') as write_file:
        for line in lines:
            write_file.write(line)


