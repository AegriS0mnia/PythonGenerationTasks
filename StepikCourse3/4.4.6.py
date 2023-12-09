import json
import sys


def json_reader():
    lines = ''
    for line in sys.stdin:
        lines += line.strip()
    return lines


json_dict = json.loads(json_reader())

for key in json_dict:
    if type(json_dict[key]) == list:
        print(f'{key}: {", ".join((str(i) for i in json_dict[key]))}')
    else:
        print(f'{key}: {json_dict[key]}')
