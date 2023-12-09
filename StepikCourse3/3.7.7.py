import calendar

years_quantity = int(input())

for i in range(years_quantity):
    year = int(input())
    print(calendar.isleap(year))
