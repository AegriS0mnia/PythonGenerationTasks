import sys
from collections import Counter

marks = Counter()

for line in sys.stdin:
    _user = line.split()
    marks[_user[0]] = int(_user[1])

print(marks.most_common()[-2][0])

