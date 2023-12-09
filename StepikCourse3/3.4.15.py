from datetime import datetime
from datetime import timedelta

date = datetime.strptime(input(), '%d.%m.%Y')
previous_day = datetime.strftime(date - timedelta(days=1), '%d.%m.%Y')
next_day = datetime.strftime(date + timedelta(days=1), '%d.%m.%Y')

print(previous_day, next_day, sep='\n')
