matrix = []

for i in range(8):
    matrix.append(['.'.ljust(3)] * 8)

position = input()
Y1, X1 = 8 - int(position[1]), ord(position[0]) - ord('a')

matrix[Y1][X1] = 'Q'.ljust(3)


for i in range(8):
    for j in range(8):
        if (X1 - i == 0 or Y1 - j == 0) or ((X1 - i)**2 == (Y1 - j)**2):
            matrix[j][i] = '*'.ljust(3)

matrix[Y1][X1] = 'Q'.ljust(3)

for i in matrix:
    print(''.join(i))