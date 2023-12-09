from datetime import date


def saturdays_between_two_dates(date1, date2):
    date1, date2 = min(date1, date2), max(date1, date2)

    date_difference = abs(date2.toordinal() - date1.toordinal())

    dates = [date.fromordinal(date1.toordinal() + i) for i in range(date_difference + 1)]
    saturdays = len(list(filter(lambda date: date.weekday() == 5, dates)))

    return saturdays
