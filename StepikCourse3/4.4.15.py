import json

with open('food_services.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    districts = set(_dict['District'] for _dict in json_data)
    nets = set(_dict['OperatingCompany'] for _dict in json_data if _dict['IsNetObject'] == 'да')
    cafes_count = {district: 0 for district in districts}
    nets_count = {net: 0 for net in nets}

    for adm_area in districts:
        for _dict in json_data:
            if _dict['District'] == adm_area:
                cafes_count[adm_area] += 1

    for net in nets:
        for _dict in json_data:
            if _dict['OperatingCompany'] == net:
                nets_count[net] += 1

    most_popular = max(cafes_count, key=lambda cafe: cafes_count[cafe])
    most_popular_net = max(nets_count, key=lambda net: nets_count[net])

    print(most_popular, cafes_count[most_popular], sep=': ')
    print(most_popular_net, nets_count[most_popular_net], sep=': ')
