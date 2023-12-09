def to_binary(number):
    if number <= 1:
        return number
    else:
        return str(to_binary(number // 2)) + str(number % 2)
