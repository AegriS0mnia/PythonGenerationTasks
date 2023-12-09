def hash_function(obj):
    if obj is None:
        obj = 'None'

    if isinstance(obj, (int, float)):
        obj = str(obj)

    def flatten(obj):
        flat_list = []
        for index, value in enumerate(obj):
            if isinstance(value, (list, tuple)):
                return flatten(value)
            if isinstance(value, (int, float, str)):
                value = str(value)
                flat_list += list(value)
        return flat_list

    objects = flatten(obj)

    temp1 = sum((ord(objects[i]) * ord(objects[-i - 1]) for i in range((len(objects)) // 2)))
    if len(objects) % 2:
        temp1 += ord(objects[len(objects) // 2])

    temp2 = sum((ord(v) * (i + 1) * (-1) ** (i % 2) for i, v in enumerate(objects)))

    result = (temp1 * temp2) % 123456791
    return result


# TEST_5:
array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

for obj in array:
    print(hash_function(obj))