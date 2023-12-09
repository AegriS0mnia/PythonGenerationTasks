import calendar

_date = map(int, input().split('-'))

print(calendar.day_name[calendar.weekday(*_date)])
