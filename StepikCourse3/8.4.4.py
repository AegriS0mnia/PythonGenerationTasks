def recursive_sum(_list):
    _sum = 0
    for i in _list:
        if isinstance(i, int):
             _sum += i
        else:
            _sum += recursive_sum(i)
    return _sum
