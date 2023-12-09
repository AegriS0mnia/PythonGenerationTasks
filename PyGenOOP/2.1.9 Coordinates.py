import sys

for line in sys.stdin:
    line = eval(line.strip())
    answer = abs(line[0]) <= 90 and abs(line[1]) <= 180
    print(answer)
    