import sys
import re

popularity = 0
for line in sys.stdin:
    line = line.strip()

    if re.search(r'^(beegeek).*(beegeek)$', line):
        popularity += 3
        continue
    if re.search(r'^(beegeek).*', line) or re.search(r'.*(beegeek)$', line):
        popularity += 2
        continue

    if re.search(r'.+(beegeek).+$', line):
        popularity += 1
        continue
else:
    print(popularity)