def same_parity(numbers):
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))
