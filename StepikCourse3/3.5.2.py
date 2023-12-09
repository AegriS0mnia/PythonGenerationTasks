from datetime import timedelta
from datetime import datetime

days = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
start = datetime(day=1, month=1, year=1)
stop = datetime(day=31, month=12, year=9999)

for day in range((stop - start).days):
    _day = start.weekday()
    if start.day == 13:
        days[_day] += 1
    start += timedelta(days=1)

for key in days:
    print(days[key])
