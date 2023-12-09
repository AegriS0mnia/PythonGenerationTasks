import calendar

cool_list = input().split()
month = list(calendar.month_name).index(cool_list[1])
print(calendar.monthrange(int(cool_list[0]), month)[1])
