def recursive_sum(first_number, second_number):
    if second_number <= 0:
        return first_number
    else:
        return recursive_sum(first_number + 1, second_number - 1)
