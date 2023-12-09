from datetime import timedelta
from datetime import datetime

time = datetime.strptime(input(), '%H:%M:%S')
seconds = timedelta(seconds=int(input()))
stop_value = time + seconds

answer = stop_value.strftime('%H:%M:%S')

print(answer)