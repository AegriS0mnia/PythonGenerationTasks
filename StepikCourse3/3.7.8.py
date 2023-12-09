import calendar

months = dict(zip(list(calendar.month_abbr), (i for i in range(13))))
year, month = input().split()

print(calendar.month(int(year), months[month]))
