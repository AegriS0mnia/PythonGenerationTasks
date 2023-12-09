import json

with open('data.json', 'r', encoding='utf-8') as _input, open('updated_data.json', 'w', encoding='utf-8') as _output:
    lines = json.load(_input)

    lines = list(filter(lambda obj: obj != None, lines))

    for i in range(len(lines)):
        if isinstance(lines[i], str):
            lines[i] = lines[i] + '!'
        elif type(lines[i]) == bool:
            lines[i] = not(lines[i])
        elif isinstance(lines[i], (int, float)):
            lines[i] += 1
        elif isinstance(lines[i], list):
            lines[i] *= 2
        elif isinstance(lines[i], dict):
            lines[i].setdefault('newkey', None)

    json.dump(lines, _output)