import sys

lines = []

for line in sys.stdin:
    if not(line.strip().startswith('#')):
        lines.append(line.rstrip())
    elif line.isspace():
        lines.append('\n')

print(*lines, sep='\n')
