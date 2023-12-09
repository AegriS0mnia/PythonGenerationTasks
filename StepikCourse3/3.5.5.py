from datetime import datetime

employee_number = int(input())
employees = []

for i in range(employee_number):
    employee = input().split()
    employee_data = [employee[0], employee[1], datetime.strptime(employee[2], '%d.%m.%Y')]
    employees.append(employee_data)

the_oldest = min(employees, key=lambda emp: emp[2])

old_men = tuple(filter(lambda emp: emp[2] == the_oldest[2], employees))

if len(old_men) < 2:
    print(f'{the_oldest[2].strftime("%d.%m.%Y")} {the_oldest[0]} {the_oldest[1]}')
else:
    print(f'{the_oldest[2].strftime("%d.%m.%Y")} {len(old_men)}')
