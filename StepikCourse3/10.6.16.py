def is_prime(number):
    denominators = any(i for i in range(2, number // 2) if number % i == 0)
    if number == 1:
        return False
    if denominators:
        return False
    return True
