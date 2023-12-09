size = int(input())

matrix = [[int(i) for i in input().split()] for i in range(size)]

flag = True

for i in range(size):
    for j in range(size):
        if j != size - 1 - i:
            if matrix[i][j] != matrix[size-j-1] [size-i-1]:
                flag = False

if flag:
    print('YES')
else:
    print('NO')