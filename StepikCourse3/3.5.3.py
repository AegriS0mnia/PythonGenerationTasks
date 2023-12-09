from datetime import timedelta
from datetime import datetime

schedule = {0: (timedelta(hours=9), timedelta(hours=21)),
            1: (timedelta(hours=9), timedelta(hours=21)),
            2: (timedelta(hours=9), timedelta(hours=21)),
            3: (timedelta(hours=9), timedelta(hours=21)),
            4: (timedelta(hours=9), timedelta(hours=21)),
            5: (timedelta(hours=10), timedelta(hours=18)),
            6: (timedelta(hours=10), timedelta(hours=18)), }

_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
_weekday = _date.weekday()


is_opened = schedule[_weekday][1].seconds // 3600 > _date.hour >= schedule[_weekday][0].seconds // 3600
work_time = (schedule[_weekday][1].seconds - (_date.hour * 3600 + _date.minute * 60)) // 60

if is_opened:
    print(work_time)
else:
    print('Магазин не работает')
