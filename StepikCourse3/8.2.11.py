def hourglass(number=0):
    if number < 4:
        print('  ' * number + (str(1 + number) * (16 - 4 * number)))
        hourglass(number + 1)
    if number < 2:
        return 0
    print('  ' * (-2 + number) + (str(-1 + number) * (24 - 4 * number)))


hourglass()
