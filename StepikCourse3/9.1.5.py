def convert(number):
    if number >= 0:
        return bin(number)[2:], oct(number)[2:], hex(number)[2:].upper()
    else:
        return f'-{bin(number)[3:]}', f'-{oct(number)[3:]}', f'-{hex(number)[3:].upper()}'
