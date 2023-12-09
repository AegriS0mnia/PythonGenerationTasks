def custom_isinstance(objects, typeinfo):
    return list(map(lambda obj: isinstance(obj, typeinfo), objects)).count(True)
