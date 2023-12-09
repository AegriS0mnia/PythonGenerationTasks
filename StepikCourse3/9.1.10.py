def is_greater(lists, number):
    return any(map(lambda lst: sum(lst) > number, lists))
