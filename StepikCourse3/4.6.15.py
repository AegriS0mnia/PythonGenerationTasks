import pickle

filename, checksum = input(), int(input())

with open(filename, 'rb') as binary_file:
    deserialized_file = pickle.load(binary_file)
    _sum = 0

    if isinstance(deserialized_file, dict):
        for i in deserialized_file:
            if isinstance(i, int):
                _sum += i
    elif isinstance(deserialized_file, list):
        nums = list(filter(lambda obj: isinstance(obj, int), deserialized_file))
        if nums:
            _sum = min(*nums, 10 ** 17) * max(*nums, -10 ** 17)
        else:
            _sum = 0
    if _sum == checksum:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')
