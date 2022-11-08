matrix = [
    [1, 4, 3],  # 0
    [7, 9, 2],  # 1
    [5, 0, -8],  # 2
]

for line in range(len(matrix)):
    for elem in range(len(matrix[line])):
        print(matrix[line][elem], end=' ')
    print()
