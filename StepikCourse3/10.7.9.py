from datetime import date, timedelta

def years_days(year):
    start = date(year=year, month=1, day=1)
    end = date(year=year, month=12, day=31)

    while start <= end:
        yield start
        start += timedelta(days=1)
