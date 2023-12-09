def print_nums(num=100):
    if num > 0:
        print_nums(num - 1)
        print(num)

print_nums()