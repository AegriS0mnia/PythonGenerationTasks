import sys
import re

pattern = r'_\d+[a-zA-Z]*_?'

for line in sys.stdin:
    line = line.strip()

    is_valid_login = bool(re.fullmatch(pattern, line))

    print(is_valid_login)

