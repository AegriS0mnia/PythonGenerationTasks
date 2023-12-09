def is_power(number):
    if number <= 2:
        return True
    if number % 2 == 1:
        return False
    else:
        return is_power(number // 2)
