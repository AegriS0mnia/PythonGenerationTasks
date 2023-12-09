def traffic(number):
    if number > 0:
        traffic(number - 1)
        print('Не парковаться')
c