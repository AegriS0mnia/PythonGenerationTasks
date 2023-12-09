def number_of_frogs(year):
    if year == 1:
        return 77
    else:
        return 3 * (number_of_frogs(year - 1) - 30)

