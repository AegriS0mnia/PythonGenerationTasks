size = int(input())

matrix = [[int(i) for i in input().split()] for i in range(size)]
_max = -10**19
if size == 1:
    _max, = matrix[0]
else:
    for i in range(size):
        for j in range(size):
            if j >= size - i - j:
                _max = max(_max, matrix[i][j])

print(_max)