from datetime import date
from datetime import timedelta

cools_nums = int(input()), int(input())
_date = date(year=cools_nums[0], month=cools_nums[1], day=1)

if cools_nums[1] == 12:
    next_month = date(year=cools_nums[0] + 1, month=1, day=1)
else:
    next_month = date(year=cools_nums[0] + 1, month=1, day=1)
counter = 0

while _date <= next_month:
    if _date.weekday() == 3:
        counter += 1
    if counter == 4:
        print(_date.strftime('%d.%m.%Y'))
        break
    _date += timedelta(days=1)
