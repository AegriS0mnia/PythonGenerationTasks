size = int(input())

matrix = [[int(i) for i in input().split()] for i in range(size)]
vector = [int(i) for i in range(1, size + 1)]

flag = True
for i in range(size):
    temp_row = []
    temp_column = []
    for j in range(size):
        temp_row.append(matrix[i][j])
        temp_column.append(matrix[j][i])
    if sorted(temp_row) != vector or sorted(temp_column) != vector:
        flag = False

if flag:
    print('YES')
else:
    print('NO')
