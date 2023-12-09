import csv

with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
    lines = list(csv.reader(csv_file, delimiter=';'))

    header = lines.pop(0)

    keys = set()
    wifis = []

    for line in lines:
        keys.add(line[1])


    for key in keys:
        _sum = 0
        for line in lines:
            if key in line:
                 _sum += int(line[-1])
        wifis.append([key, _sum])
    wifis = sorted(wifis)
    wifis = sorted(wifis, key=lambda x: x[1], reverse=True)

    for wifi in wifis:
        if wifi != wifis[-1]:
            print(f'{wifi[0]}: {wifi[1]}')
        else:
            print(f'{wifi[0]}: {wifi[1]}', end='')
