size = int(input())
matrix = [[int(i) for i in input().split()] for i in range(size)]
new_rows = []

for i in range(size):
    temp_row = []
    for j in range(size):
        temp_row.append(matrix[j][i])
    new_rows.append(temp_row)

for row in new_rows:
    print(*row)