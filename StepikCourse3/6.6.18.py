from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = OrderedDict()
for i in range(len(data)):
    if i % 2 == 0:
        pair = data.popitem(last=False)
    else:
        pair = data.popitem()
    new_data.setdefault(*pair)


print(new_data)