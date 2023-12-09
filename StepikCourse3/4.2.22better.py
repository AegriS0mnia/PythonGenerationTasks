import csv

with open('prices.csv', 'r', encoding='utf-8') as csv_file:
    _dicts = list(csv.DictReader(csv_file, delimiter=';'))

    for _dict in _dicts:
        for key in _dict:
            try:
                _dict[key] = [int(_dict[key]), _dict['Магазин']] #Меняем строки на числа и
            except ValueError:                                   #в качестве значения сохраняем пару цена-магазин
                pass
        del _dict['Магазин'] #удаляем список магазинов, так как они уже сохранены на предыдущем шаге

    first_dict = _dicts[0]

    min_prices = {}

    for key in first_dict:
        min_price = first_dict[key]
        for _dict in _dicts:
            min_price = min(min_price, _dict[key], key=lambda x: (x[0], x[1]))
        min_prices.setdefault(key, min_price)

for food in min_prices:
    print(f'{food}: {min_prices[food][1]}')
