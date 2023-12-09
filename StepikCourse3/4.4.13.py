import json
from datetime import datetime

with open('pools.json', encoding='utf-8') as json_file:
    json_data = list(json.load(json_file))

    flag = True

    while flag:
        for _dict in json_data:
            flag = False

            monday_worktime = _dict['WorkingHoursSummer']['Понедельник'].split('-')
            monday_opening_time = datetime.strptime(monday_worktime[0], '%H:%M').hour
            monday_closing_time = datetime.strptime(monday_worktime[1], '%H:%M').hour

            if monday_opening_time > 10 or monday_closing_time < 12:
                flag = True
                del json_data[json_data.index(_dict)]

    best_choice = max(json_data, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
    print(f'''{best_choice['DimensionsSummer']['Length']}x{best_choice['DimensionsSummer']['Width']}
{best_choice['Address']}''')
