from datetime import datetime
from datetime import timedelta


def fill_up_missing_dates(dates):
    _dates = sorted([datetime.strptime(_date, '%d.%m.%Y') for _date in dates])

    for i in range(len(_dates) - 1):
        missing_dates = [(_dates[i] + timedelta(days=j)) for j in range((_dates[i + 1] - _dates[i]).days)]

        for i in missing_dates:
            _dates.append(i)

    _dates = sorted(set([datetime.strftime(i, '%d.%m.%Y') for i in _dates]))

    return _dates
