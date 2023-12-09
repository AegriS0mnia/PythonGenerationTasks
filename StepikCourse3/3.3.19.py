from datetime import datetime


def split_dates(dates):

    _dates_ = []

    if isinstance(dates, str):
        if '-' in dates:
            date = dates.split('-')
            start, end = datetime.strptime(date[0], '%d.%m.%Y').toordinal(), datetime.strptime(date[1], '%d.%m.%Y').toordinal()
            while start <= end:
                _dates_.append(datetime.fromordinal(start))
                start += 1
        else:
            _dates_.append(datetime.strptime(dates, '%d.%m.%Y'))
    else:
        for i in range(len(dates)):

            if '-' in dates[i]:
                date = dates[i].split('-')
                start, end = datetime.strptime(date[0], '%d.%m.%Y').toordinal(), datetime.strptime(date[1], '%d.%m.%Y').toordinal()
                while start <= end:
                    _dates_.append(datetime.fromordinal(start))
                    start += 1
            else:
                _date = datetime.strptime(dates[i], '%d.%m.%Y')
                _dates_.append(_date)


    return _dates_


def is_available_date(booked_dates, date_for_booking):
    _booked_dates = set(split_dates(booked_dates))
    _date_for_booking = set(split_dates(date_for_booking))

    if _date_for_booking.isdisjoint(_booked_dates):
        return True
    else:
        return False