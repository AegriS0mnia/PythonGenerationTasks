import csv

with open('deniro.csv', 'r', encoding='utf-8') as csv_file:
    lines = list(csv.reader(csv_file))
    key = int(input()) - 1

    lines = sorted(lines, key=lambda x: int(x[key]) if x[key].isdigit() else x[key])

    for line in lines:
        print(','.join(line))
