import json
from zipfile import ZipFile


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


players = []

with ZipFile('data.zip') as zip_file:
    infolist = zip_file.infolist()

    for file in infolist:
        is_file = not (file.is_dir())

        if is_file:
            with zip_file.open(file.filename) as file:
                _file = file.read()

                try:
                    is_json = is_correct_json(_file)
                    if is_json:
                        json_file = json.loads(_file)
                        if json_file['team'] == 'Arsenal':
                            players.append((json_file['first_name'], json_file['last_name']))
                except UnicodeDecodeError:
                    continue
players.sort(key=lambda x: (x[0], x[1]))

for i in players:
    print(*i)
