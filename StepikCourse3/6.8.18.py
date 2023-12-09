import csv
from collections import Counter

with open('name_log.csv', encoding='utf-8') as csv_file:
    csv_data = list(csv.DictReader(csv_file))
    print(*csv_data, sep='\n')
    ct = Counter(csv_data[0])
    print(ct)
