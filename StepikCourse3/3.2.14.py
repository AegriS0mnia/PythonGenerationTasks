from datetime import date

def print_good_dates(dates):
    good_dates = sorted([date for date in dates if date.year == 1992 and date.month + date.day == 29])
    formated_dates = [date.strftime('%B %d, %Y') for date in good_dates]

    print(*formated_dates, sep='\n')






dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)