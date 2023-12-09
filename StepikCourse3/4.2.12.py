import csv

with open('sales.csv', 'r', encoding='utf-8') as csv_file:
    lines = list(csv.reader(csv_file, delimiter=';'))
    del lines[0]

    lines = list(filter(lambda price: int(price[1]) > int(price[2]), lines))

    for line in lines:
        print(line[0])
