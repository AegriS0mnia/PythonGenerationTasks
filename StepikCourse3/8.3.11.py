def get_fast_pow(number, pow):
    if pow == 0:
        return 1
    if pow == 1:
        return number
    elif pow % 2 == 1:
        return number * get_fast_pow(number, pow - 1)
    elif pow % 2 == 0:
        return get_fast_pow(number * number, pow // 2)
