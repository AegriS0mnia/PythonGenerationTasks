import calendar
from datetime import date


def get_days_in_month(year, month):
    _month = list(calendar.month_name).index(month)
    dates = [date(year, _month, day=i) for i in range(1, calendar.monthrange(year, _month)[1] + 1)]

    return dates
