from datetime import timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

time = 0
for i in data:
    local_start = tuple(map(int, i[0].split(':')))
    local_stop = tuple(map(int, i[1].split(':')))
    time_diff = timedelta(hours=local_stop[0], minutes=local_stop[1]) - timedelta(hours=local_start[0],
                                                                                  minutes=local_start[1])
    time += time_diff.seconds

print(time // 60)
