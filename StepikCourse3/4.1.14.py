import sys

counter = 0

for line in sys.stdin:
    if line.strip().startswith('#'):
        counter += 1

print(counter)
