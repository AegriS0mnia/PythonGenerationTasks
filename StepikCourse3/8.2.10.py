def triangle(h=1):
    if h > 0:
        triangle(h - 1)
        print('*' * h)
