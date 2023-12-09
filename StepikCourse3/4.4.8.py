import json

with open('4.8data1.json', encoding='utf-8') as input_1, open('4.8data2.json') as input_2:
    with open('data_merge.json', 'w', encoding='utf-8') as output:
        dict_1 = json.load(input_1)
        dict_2 = json.load(input_2)

        dict_1.update(dict_2)

        json.dump(dict_1, output)
