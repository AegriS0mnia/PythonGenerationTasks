from datetime import timedelta
from datetime import datetime

_date = datetime.strptime(input(), '%H:%M:%S')
seconds = timedelta(hours=_date.hour, minutes=_date.minute, seconds=_date.second).total_seconds()

print(int(seconds))
