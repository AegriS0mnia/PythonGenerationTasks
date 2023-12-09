from datetime import datetime
from datetime import timedelta


def choose_plural(amount, declesions):
    if 11 <= amount % 100 <= 19:
        return (amount, declesions[2])
    elif amount % 10 == 1:
        return (amount, declesions[0])
    elif 1 < amount % 10 < 5:
        return (amount, declesions[1])
    else:
        return (amount, declesions[2])


declesions_days = ['день', 'дня', 'дней']
declesions_hours = ['час', 'часа', 'часов']
declesions_minutes = ['минута', 'минуты', 'минут']

_date_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
release = datetime(year=2022, month=11, day=8, hour=12)
time_diff = release - _date_time

days = choose_plural(time_diff.days, declesions_days)
hours = choose_plural(time_diff.seconds // 3600, declesions_hours)
minutes = choose_plural(time_diff.seconds % 3600 // 60, declesions_minutes)

time = [i for i in (days, hours, minutes) if i[0] > 0]
if days[0] > 0 and hours[0] > 0 and minutes[0] > 0:
    del time[time.index(minutes)]

if _date_time >= release:
    print('Курс уже вышел!')
else:
    print('До выхода курса осталось: ', end='')

    for i in time:

        if i[0] > 0 and i != time[0]:
            print(f' и {i[0]} {i[1]}', end='')
        else:
            print(f'{i[0]} {i[1]}', end='')
