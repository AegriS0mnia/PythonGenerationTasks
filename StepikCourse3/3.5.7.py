from datetime import datetime
from datetime import timedelta

_date = datetime.strptime(input(), '%d.%m.%Y')

nearest_dates = [(datetime.fromordinal(_date.toordinal() + i).month, datetime.fromordinal(_date.toordinal() + i).day) for i in range(1, 8)]

employee_number = int(input())
employees = []
filtered_data = []


for i in range(employee_number):
    employee = input().split()
    employee_data = [employee[0], employee[1], datetime.strptime(employee[2], '%d.%m.%Y')]
    employees.append(employee_data)

for i in employees:
    print((i[2].month, i[2].day))
    print(i[2])
    if (i[2].month, i[2].day) in nearest_dates:
        filtered_data.append(i)

if filtered_data:
    print(*max(filtered_data, key=lambda x: x[2])[:-1])
else:
    print('Дни рождения не планируются')