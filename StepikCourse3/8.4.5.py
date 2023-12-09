def linear(_list):
    new_list = []

    for i in _list:
        if isinstance(i, int):
            new_list.append(i)
        else:
            new_list += linear(i)

    return new_list
