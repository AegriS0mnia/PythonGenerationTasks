from datetime import datetime
from collections import defaultdict

employee_number = int(input())
employees = defaultdict(int)

for i in range(employee_number):
    employee = input().split()
    employee_birthday = datetime.strptime(employee[2], '%d.%m.%Y')
    employees[employee_birthday] += 1

sorted_keys = sorted(employees)

for key in sorted_keys:
    if employees[key] == max(employees.values()):
        print(key.strftime('%d.%m.%Y'))
