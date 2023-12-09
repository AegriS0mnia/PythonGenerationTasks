from datetime import date, timedelta
from typing import Generator

def dates(start_date: date, count: int=None) -> Generator:
    current_date: date = start_date


    if not (count is None):
        for i in range(count):
            if current_date == date.max:
                yield date(9999, 12, 31)
                break
            yield current_date
            current_date += timedelta(days=1)
    else:
        while True:
            if current_date == date.max:
                yield date(9999, 12, 31)
                break
            yield current_date
            current_date += timedelta(days=1)
