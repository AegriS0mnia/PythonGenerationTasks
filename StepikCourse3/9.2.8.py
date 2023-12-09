def hash_as_key(objects):
    hashes_objects = tuple([(hash(i), i) for i in objects])
    keys = (i[0] for i in hashes_objects)
    result = {}

    for key in keys:
        temp_list_of_values = []
        for _hash in hashes_objects:
            if _hash[0] == key:
                temp_list_of_values.append(_hash[1])

        if len(temp_list_of_values) == 1:
            result.setdefault(key, *temp_list_of_values)
        else:
            result.setdefault(key, temp_list_of_values)

    return result
