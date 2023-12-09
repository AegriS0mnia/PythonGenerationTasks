from collections import defaultdict

def flip_dict(_dict):
    new_keys = []
    for iterable in _dict.values():
        for elem in iterable:
            if elem not in new_keys:
                new_keys.append(elem)
    flipped_dict = {key: [] for key in new_keys}

    for key in flipped_dict:
        for k in _dict:
            if key in _dict[k]:
                flipped_dict[key].extend([k] * _dict[k].count(key))

    return defaultdict(list, flipped_dict.items())
