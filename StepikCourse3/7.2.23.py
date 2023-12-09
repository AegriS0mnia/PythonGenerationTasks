import sys
from decimal import Decimal
from decimal import InvalidOperation

_sum = 0
counter = 0

for line in sys.stdin:
    try:
        _sum += Decimal(line)
    except InvalidOperation:
        counter += 1

print(_sum, counter, sep='\n')
