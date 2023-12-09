n, X, Y, A, B = map(int, input().split())
sequence = [i for i in range(1, n + 1)]

sequence[X - 1: Y] = sequence[X - 1: Y][::-1]
sequence[A - 1: B] = sequence[A - 1:B][::-1]

print(*sequence)
