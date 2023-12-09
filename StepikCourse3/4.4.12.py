import json
import csv

with open('students.json', encoding='utf-8') as json_file, open('4.4.12.csv', 'w', encoding='utf-8') as _4_4_12_csv:
    json_data = json.load(json_file)

    filtered_json_data = list(filter(lambda info: info['age'] >= 18 and info['progress'] >= 75, json_data))



    for _dict in filtered_json_data:
        print(_dict['name'], _dict['phone'], sep=',',  file=_4_4_12_csv)

with open('4.4.12.csv', 'r', encoding='utf-8') as csv_data, open('4.4.8data.csv', 'w', encoding='utf-8') as csv_output:

    lines = list(csv.reader(csv_data))
    lines = sorted(lines, key=lambda student: student[0])

    headers = 'name,phone'

    print(headers, file=csv_output)

    for line in lines:
        print(line[0], line[1], sep=',', file=csv_output)
