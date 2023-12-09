def triangle(h=1):
    if h > 0:
        print('*' * h)
        triangle(h-1)
