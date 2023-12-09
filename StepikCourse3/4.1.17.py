import sys
from datetime import datetime

dates = []

for _date in sys.stdin:
    _date_ = datetime.strptime(_date.strip(), '%d.%m.%Y')
    dates.append(_date_)

ASC = []
DESC = []

for i in range(1, len(dates)):
    if dates[i - 1] < dates[i]:
        ASC.append(True)
        DESC.append(False)
    elif dates[i - 1] > dates[i]:
        DESC.append(True)
        ASC.append(False)
    else:
        ASC.append(False)
        DESC.append(False)
        break


if all(ASC):
    print('ASC')
elif all(DESC):
    print('DESC')
else:
    print('MIX')
