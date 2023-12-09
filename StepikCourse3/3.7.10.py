import calendar

some_cool_numbers = map(int, input().split())

print(calendar.monthrange(*some_cool_numbers)[1])
