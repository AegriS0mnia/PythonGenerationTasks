size = int(input())

matrix = [[1] * size for i in range(size)]

for k in range(1, size - 1): #Количество увеличений на 1
    for i in range(k, size - k):
        for j in range(k, size - k):
            matrix[i][j] += 1

for row in matrix:
    print(*row)