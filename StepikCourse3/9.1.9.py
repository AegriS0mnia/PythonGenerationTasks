def non_negative_even(numbers):
    return all(map(lambda num: num >= 0 and abs(num) % 2 == 0, numbers))
