def print_numbers(num=0):
    num = int(input())

    if num == 0:
        return print(0)
    if num != 0:
        print_numbers(num)
    print(num)


print_numbers()
