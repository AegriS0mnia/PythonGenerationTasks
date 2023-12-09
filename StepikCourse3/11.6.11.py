import sys
import re

pattern = r"(\w+)\1"

for line in sys.stdin:
    line = line.strip()

    is_valid_word = bool(re.fullmatch(pattern, line))

    if is_valid_word:
        print(line)
