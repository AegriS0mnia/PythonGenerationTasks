import sys

moves = []

for line in sys.stdin:
    moves.append(int(line.strip()))

if (moves[-1] % 2 == 0 and len(moves) % 2 == 1) or (len(moves) % 2 == 0 and moves[-1] % 2 == 1):
    print('Анри')
else:
    print('Дима')

