def flatten(nested_list):
    new_list = []

    if isinstance(nested_list, int):
        new_list.append(nested_list)
    if isinstance(nested_list, list):
        for i in nested_list:
            new_list += flatten(i)
    yield from new_list
