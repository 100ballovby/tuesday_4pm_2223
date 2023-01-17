def to_array(path):
    arr = []
    with open(path) as file:
        lns = file.readlines()
        for line in lns:
            arr.append(line.strip())
    return arr

print(to_array('alice.txt'))


