size = int(input())
matrix = [[0] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        if i != j:
            matrix[i][j],  matrix[j][i] = abs(i - j), abs(i - j)

for row in matrix:
    print(*row)
