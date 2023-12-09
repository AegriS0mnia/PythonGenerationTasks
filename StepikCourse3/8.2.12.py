def print_digits(number):
    if number:
        print_digits(number // 10)
        print(number % 10)

