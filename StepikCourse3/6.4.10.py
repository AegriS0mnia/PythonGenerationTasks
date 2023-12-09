import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', 'rb') as binary_data:
    deserialized_data = pickle.load(binary_data)

    for _tuple in deserialized_data:
        _tuple = _tuple._asdict()
        for key in _tuple:
            print(f'{key}: {_tuple[key]}')
        print()
