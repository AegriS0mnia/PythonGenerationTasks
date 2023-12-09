import sys

values = []

for line in sys.stdin:
    values.append(eval(line))

print(max(values))
