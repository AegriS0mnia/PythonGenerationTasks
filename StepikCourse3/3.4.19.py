from datetime import datetime
from datetime import timedelta

_date = datetime.strptime(input(), '%d.%m.%Y')
previous_date = _date

print(_date.strftime('%d.%m.%Y'))
for i in range(2, 11):

    _date = previous_date + timedelta(days=i)
    previous_date = _date
    print(previous_date.strftime('%d.%m.%Y'))
