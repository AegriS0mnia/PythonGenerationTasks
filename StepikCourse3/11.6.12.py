import sys
import re

pattern_1 = r".*bee.*bee.*"
pattern_2 = r'.*\bgeek\b.*'
bees, geeks = 0, 0

for line in sys.stdin:
    line = line.strip()

    bees += bool(re.fullmatch(pattern_1, line))
    geeks += bool(re.fullmatch(pattern_2, line))

else:
    print(bees, geeks, sep='\n')
