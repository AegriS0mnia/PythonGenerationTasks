from datetime import timedelta

line1, line2 = list(map(int, input().split(':'))), list(map(int, input().split(':')))

start, stop = timedelta(hours=line1[0], minutes=line1[1]), timedelta(hours=line2[0],
                                                                     minutes=line2[1])

previous_time = start
times = [start]

while stop - previous_time >= timedelta(minutes=45):
    _time = previous_time + timedelta(minutes=45)
    previous_time = _time + timedelta(minutes=10)

    times.extend([_time, previous_time])

del times[-1]

for i in range(1, len(times), 2):
    print(
        f"{str(times[i - 1].seconds // 3600).rjust(2, '0')}:{str(times[i - 1].seconds % 3600 // 60).rjust(2, '0')} - {str(times[i].seconds // 3600).rjust(2, '0')}:{str(times[i].seconds % 3600 // 60).rjust(2, '0')}")
