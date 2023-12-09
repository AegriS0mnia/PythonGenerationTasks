from datetime import date

date1, date2 = date.fromisoformat(input()), date.fromisoformat(input())

min_date = min(date1, date2)

print(min_date.strftime('%d-%m (%Y)'))