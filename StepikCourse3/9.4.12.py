old_print = print


def new_print(*args, sep=' ', end='\n'):
    for i in args:
        if isinstance(i, str):
            old_print(i.upper(), sep='', end='', )
        else:
            old_print(i, sep='', end='', )

        if i != args[-1]:
            old_print(sep.upper(), sep='', end='')
        else:
            old_print(end.upper(), sep='', end='')


print = new_print
