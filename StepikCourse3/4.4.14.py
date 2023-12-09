import csv
import json
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as csv_file, open('best_scores.json', 'w',
                                                                  encoding='utf-8') as json_output:
    _dicts = list(csv.DictReader(csv_file))
    best_scores = []
    names = set()
    for _dict in _dicts:
        names.add((_dict['name'], _dict['surname']))

    for name in names:
        temp_list = []
        for _dict in _dicts:
            if _dict['name'] in name and _dict['surname'] in name:
                new_dict = dict(
                    [('name', _dict['name']), ('surname', _dict['surname']), ('best_score', int(_dict['score'])),
                     ('date_and_time', _dict['date_and_time']), ('email', _dict['email'])])

                temp_list.append(new_dict)
        best_score = max(temp_list, key=lambda _dict: (
            _dict['best_score'], datetime.strptime(_dict['date_and_time'], '%Y-%m-%d %H:%M:%S')))

        best_scores.append(best_score)

    best_scores = sorted(best_scores, key=lambda d: d['email'])
    json.dump(best_scores, json_output, indent=3)
