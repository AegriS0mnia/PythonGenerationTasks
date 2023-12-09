def count_digits(num):
    if num < 10:
        return 1
    else:

        return 1 + count_digits(num // 10)

print(count_digits(int(input())))