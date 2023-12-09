from datetime import datetime
from collections import namedtuple
import csv

with open('meetings.csv', 'r', encoding='utf-8') as data:
    lines = list(csv.reader(data))
    fields = lines.pop(0)
    Friend = namedtuple('Friend', fields)

    friends = []

    for meeting in lines:
        meet_date = datetime.strptime(f'{meeting[2]} {meeting[3]}', '%d.%m.%Y %H:%M')
        _meeting = (meeting[0], meeting[1], meet_date, None)
        friends.append(Friend._make(_meeting))

    friends.sort(key=lambda friend: friend[2])

    for i in friends:
        print(i[0], i[1])
