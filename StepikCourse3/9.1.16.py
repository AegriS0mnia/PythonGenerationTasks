import string


def unusual_sort(line):
    small_letter = sorted(i for i in line if i in string.ascii_lowercase)
    capitals = sorted(i for i in line if i in string.ascii_uppercase)
    digits = sorted(i for i in line if i in string.digits)
    evens = sorted(i for i in digits if int(i) % 2 == 0)
    odds = sorted(i for i in digits if int(i) % 2 == 1)
    return ''.join(small_letter + capitals + odds + evens)

unusual_sort(input())
