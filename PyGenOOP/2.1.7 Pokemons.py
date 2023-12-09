import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

answer = len(lines) - len(set(lines))

print(answer)