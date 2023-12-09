from datetime import datetime

def num_of_sundays(year):

    if datetime(year, 1, 1).weekday() != 0 and year % 4 == 0:
        return 53
    else:
        return 52
