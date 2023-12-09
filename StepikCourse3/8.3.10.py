def get_pow(number, pow):
    if pow == 0:
        return 1
    if pow == 1:
        return number
    else:
        return number * get_pow(number, pow - 1)
