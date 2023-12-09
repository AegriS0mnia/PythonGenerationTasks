def print_operation_table(operation, rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([0] * cols)

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            matrix[i - 1][j - 1] = operation(i, j)

    for row in matrix:
        for j in row:
            print(str(j).ljust(4, ' '), end=' ')
        print()
