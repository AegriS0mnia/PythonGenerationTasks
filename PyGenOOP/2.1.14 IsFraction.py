def is_fraction(string):
    string = string.split('/')
    if len(string) == 2 and string[1].isdigit():
        try:
            int(string[0])
            if int(string[1]) == 0:
                return False
            return True
        except ValueError:
            return False
    return False
