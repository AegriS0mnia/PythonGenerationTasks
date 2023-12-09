import random

def random_numbers(left, right):
    return iter(lambda: random.randint(left, right), left - 1)
