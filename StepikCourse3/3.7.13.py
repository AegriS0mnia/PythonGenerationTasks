import calendar
from datetime import timedelta
from datetime import date


def get_all_correct_dates(year):
    days = 366 if calendar.isleap(year) else 365
    dates = []
    start = date(year, 1, 1)
    for i in range(days):
        dates.append(start)
        start += timedelta(days=1)

    filtered_dates = list(filter(lambda _day: _day.weekday() == 3, dates))

    filtered_filtered_dates = []

    for i in range(1, 13):
        local_list = []
        for j in filtered_dates:
            if j.month == i:
                local_list.append(j)
        filtered_filtered_dates.append(local_list[2])

    for i in filtered_filtered_dates:
        print(date.strftime(i, '%d.%m.%Y'))


year = int(input())

get_all_correct_dates(year)
