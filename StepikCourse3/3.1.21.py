from datetime import date


def get_date_range(date1, date2):
    dates_difference = date2.toordinal() - date1.toordinal()

    dates = [date.fromordinal(date1.toordinal() + i) for i in range(dates_difference + 1)]
    
    return dates



date1 = date(2019, 6, 7)
date2 = date(2019, 6, 5)

print(date2.toordinal() - date1.toordinal())


print(get_date_range(date1, date2), sep='\n')