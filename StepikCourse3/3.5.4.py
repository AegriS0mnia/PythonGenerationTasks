from datetime import datetime
from datetime import timedelta


def print_good_dates(start_date):
    while start_date <= right_border:
        if (start_date.weekday() != 0) and (start_date.weekday() != 3):
            print(start_date.date().strftime('%d.%m.%Y'))
        start_date += timedelta(days=3)


left_border = datetime.strptime(input(), '%d.%m.%Y')
right_border = datetime.strptime(input(), '%d.%m.%Y')

while (left_border.day + left_border.month) % 2 == 0:
    left_border += timedelta(days=1)
else:
    print_good_dates(left_border)
