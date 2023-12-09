size = int(input())

dots = [['.'.ljust(2)] * size for i in range(size)]

for i in range(size):
    for j in range(size):
        if i == j or j == size - i - 1:
            dots[i][j] = '*'.ljust(2)
        if i == size // 2:
            dots[i][j], dots[j][i] = '*'.ljust(2), '*'.ljust(2)

for row in dots:
    print(*row)
