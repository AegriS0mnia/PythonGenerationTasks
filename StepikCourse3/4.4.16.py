import json

with open('food_services.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    objects = set(_dict['TypeObject'] for _dict in json_data)

    objects = sorted(objects)

    objects_count = {obj: () for obj in objects}
    for obj in objects:
        temp_list = []
        for _dict in json_data:
            if _dict['TypeObject'] == obj:
                temp_list.append((_dict['Name'], _dict['SeatsCount']))
        biggest = max(temp_list, key=lambda obj: obj[1])

        objects_count[obj] = biggest

    for key in objects_count:
        print(f'{key}: {objects_count[key][0]}, {objects_count[key][1]}')
