import json
import csv

with open('playgrounds.csv', encoding='utf-8') as csv_data, open('addresses.json', 'w', encoding='utf-8') as output:
    dicts = list(csv.DictReader(csv_data, delimiter=';'))

    adm_areas = {}

    for _dict in dicts:
        adm_areas[_dict['AdmArea']] = {}

    new_adm_areas = {}

    for adm_area in adm_areas:
        local_dict = {}

        for _dict in dicts:
            if adm_area in _dict.values():
                for key in _dict:
                    local_dict.setdefault(_dict['District'], [])

        for _dict in dicts:
            for key in local_dict:
                if key in _dict.values():
                    local_dict[key].append(_dict['Address'])

        new_adm_areas.setdefault(adm_area, local_dict)

    print(new_adm_areas)

    json.dump(new_adm_areas, output, ensure_ascii=False)
