def sort_priority(values, group):
    values.sort(key=lambda x: x - 10**33 if x in group else x)
    return values
