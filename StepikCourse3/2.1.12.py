def spell(*args):
    words = list(map(str.lower, args))

    _dict = {i[0]: len(max(filter(lambda x: x.startswith(i[0]), words), key=len)) for i in words}

    return _dict
