def without_cycles(number):
    if number > 0:
        print(number)
        without_cycles(number - 5)
    print(number)

without_cycles(int(input()))