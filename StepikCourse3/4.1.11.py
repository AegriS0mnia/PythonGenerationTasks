import sys
import datetime

min_date = datetime.date(9999, 3, 31)
max_date = datetime.date(1, 2, 1)

for date in sys.stdin:
    _date = datetime.date.fromisoformat(date.strip())
    max_date = max(max_date, _date)
    min_date = min(min_date, _date)


print((max_date - min_date).days)
