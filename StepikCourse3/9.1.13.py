def my_pow(number):
    return sum((int(i[1]))**i[0] for i in enumerate(str(number), 1))

