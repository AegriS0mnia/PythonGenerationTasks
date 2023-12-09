from datetime import date

dates_quantity = int(input())
dates = [date.fromisoformat(input()) for i in range(dates_quantity)]

dates = sorted(dates)

for date in dates:
    print(date.strftime('%d/%m/%Y'))
