import csv

with open('student_counts.csv', encoding='utf-8') as csv_data, open('sorted_csv_counts.csv', 'w',
                                                                    encoding='utf-8') as output:
    lines = list(csv.DictReader(csv_data))
    new_lines = []

    for _dict in lines:
        for key in _dict:
            _dict[key] = int(_dict[key])

    for _dict in lines:
        temp_dict = {}
        keys = sorted(_dict)
        year = (keys[-1], _dict[keys[-1]])
        del keys[-1]
        keys = sorted(keys, key=lambda x: int(x.split('-')[0]))

        for key in keys:
            temp_dict.setdefault(key, _dict[key])

        temp_dict.setdefault(*year)
        new_lines.append(temp_dict)

    headers = [list(new_lines[0])[-1]] + list(new_lines[0])[:len(list(new_lines)[0]) - 1]
    print(*headers, sep=',', file=output)

    for _dict in new_lines:
        print(_dict['year'], *list(_dict.values())[:-1], sep=',', file=output)
