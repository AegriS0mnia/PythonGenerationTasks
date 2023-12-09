from math import ceil


def primes(left, right):
    if left == right:
        yield left
        return
    if left == 1:
        left += 1

    def is_prime(number):
        if number == 2:
            return True

        for denom in range(2, ceil(number // 2) + 1):
            if number % denom == 0:
                return False

        return True

    for number in range(left, right + 1):
        if is_prime(number):
            yield number
