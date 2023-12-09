with open('data.csv', encoding='utf-8') as csv_file:
    csv_data = (line.rstrip().split(',') for line in csv_file)
    headers = next(csv_data)
    line_dicts = (dict(zip(headers, data)) for data in csv_data)
    round_a = (i for i in line_dicts if i['round'] == 'a')
    _sum = sum(int(i['raisedAmt']) for i in round_a)
    print(_sum)
