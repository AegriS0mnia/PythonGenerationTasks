from datetime import date


def is_correct(day, month, year):
    try:
        _date = date(year, month, day)
        return True
    except ValueError:
        return False

print(is_correct(31, 13, 2021))