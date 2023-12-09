import csv

def condense_csv(file_name, id_name):
    with open(file_name, 'r', encoding='utf-8') as csv_file, open('condensed.csv', 'w', encoding='utf-8') as output:
        lines = list(csv.reader(csv_file))
        print(*lines, sep='\n')
        objects = set()
        _dicts = []

        for line in lines:
            objects.add(line[0])

        objects = sorted(objects)

        for key in objects:
            _objects = {}
            for line in lines:
                if key in line:
                    _objects.setdefault(line[1], line[2])
            _dicts.append(_objects)


        headers = f'{id_name},{",".join(_dicts[0].keys())}'
        print(headers, file=output)

        for index, dict in enumerate(_dicts):

            if dict != _dicts[-1]:
                print(objects[index], ','.join(dict.values()), sep=',', file=output)
            else:
                print(objects[index], ','.join(dict.values()), sep=',', end='',  file=output)

condense_csv('4.2.20.csv', 'ID')