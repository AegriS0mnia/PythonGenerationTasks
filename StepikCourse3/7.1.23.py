def get_max_index(numbers):
    max_index = numbers.index(min(numbers))
    max_value = min(numbers)

    for index, value in enumerate(numbers):
        if numbers[index] > numbers[max_index]:
            max_index = index
            max_value = value

    return max_index
