def index_of_nearest(numbers, number):
    diff_of_modules = []

    for i in numbers:
        diff_of_modules.append(abs(number - i))

    filtered = list(filter(lambda x: abs(x - number) == min(diff_of_modules), numbers))

    if filtered:
        index = numbers.index(filtered[0])
    else:
        index = -1

    return index

