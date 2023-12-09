import json
from collections import defaultdict

with open('people.json', encoding='utf-8') as people_json, open('updated_people.json', 'w') as output:
    json_data = json.load(people_json)
    all_keys = defaultdict(None)

    for _dict in json_data:
        for key in _dict:
            all_keys[key] = None

    for _dict in json_data:
        for key in all_keys:
            _dict.setdefault(key, None)

    json.dump(json_data, output)