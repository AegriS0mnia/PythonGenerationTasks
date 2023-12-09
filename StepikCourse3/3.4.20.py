from datetime import datetime

dates = [datetime.strptime(_date, '%d.%m.%Y') for _date in input().split()]
days_between = []

for i in range(len(dates) - 1):
    _days_between = abs(dates[i + 1] - dates[i])
    days_between.append(_days_between.days)

print(days_between)
