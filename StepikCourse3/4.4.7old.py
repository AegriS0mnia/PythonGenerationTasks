import json

with open('data.json', 'r', encoding='utf-8') as _input, open('updated_data.json', 'w', encoding='utf-8') as _output:
    lines = json.load(_input)

    for i in range(len(lines) - 1):
        if isinstance(lines[i], str):
            lines[i] = lines[i] + '!'
        elif isinstance(lines[i], (int, float)):
            lines[i] += 1
        elif isinstance(lines[i], bool):
            if lines[i] == True:
                lines[i] = False
            else:
                lines[i] = True
        elif isinstance(lines[i], list):
            lines[i] *= 2
        elif isinstance(lines[i], dict):
            lines[i].setdefault("newkey", None)
    for i in lines:
        if i is None:
            del lines[lines.index(i)]
    json.dump(lines, _output)
