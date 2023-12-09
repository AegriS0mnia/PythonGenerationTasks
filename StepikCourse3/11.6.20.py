import sys
import re

pattern = 'beegeek'
valid_lines = 0

for line in sys.stdin:
    valid_lines += bool(re.search(pattern, line, flags=re.IGNORECASE))
else:
    print(valid_lines)