import json

with open('countries.json', encoding='utf-8') as countries_json, open('religion.json', 'w', encoding='utf-8') as output:
    json_data = json.load(countries_json)

    religions = set()

    for _dict in json_data:
        religions.add(_dict['religion'])
    religions = sorted(religions)
    religions_dict = {}

    for religion in religions:
        local_dict = []
        for _dict in json_data:
            for key in _dict:
                if _dict[key] == religion:
                    local_dict.append(_dict['country'])
        religions_dict.setdefault(religion, local_dict)

    json.dump(religions_dict, output)

