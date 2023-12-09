from datetime import datetime

try:
    number = int(input())
    try:
        print(datetime(year=1, month=number, day=1).strftime('%B'))
    except (ValueError, OverflowError):
        print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
