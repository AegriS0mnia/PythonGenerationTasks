import sys
from decimal import Decimal as D

numbers = []
for line in sys.stdin:
    numbers.append(int(line.strip()))

difference = numbers[1] - numbers[0]

quotient = D(numbers[1]) / D(numbers[0])

arithmetic = []
geometric = []


for i in range(1, len(numbers)):
    if numbers[i] - numbers[i - 1] == difference:
        arithmetic.append(True)
        geometric.append(False)
    elif D(numbers[i]) / D(numbers[i - 1]) == quotient:
        geometric.append(True)
        arithmetic.append(False)
    else:
        arithmetic.append(False)
        geometric.append(False)

if all(arithmetic):
     print('Арифметическая прогрессия')
elif all(geometric[1:]):
     print('Геометрическая прогрессия')
else:
     print('Не прогрессия')
