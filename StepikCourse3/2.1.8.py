def convert(string):
    lowercase_counter = 0
    capitals_counter = 0

    for i in string:
        if i.isalpha():
            if i == i.lower():
                lowercase_counter += 1
            else:
                capitals_counter += 1

    if capitals_counter > lowercase_counter:
        return string.upper()
    else:
        return string.lower()
