import sys
import re


pattern = r'(?P<country>\d{1,3})([- ])(?P<city>\d{1,3})\2(?P<phone>\d{4,10})'
for line in sys.stdin:
    line = line.strip()
    numbers = re.search(pattern, line).groupdict()
    print(f"Код страны: {numbers['country']}, Код города: {numbers['city']}, Номер: {numbers['phone']}")
