def print_given(*args, **kwargs):
    kwargs = sorted(kwargs.items())
    for i in args:
        print(i, type(i))

    for j in kwargs:
        print(j[0], j[1], type(j[1]))

print_given(1, [1, 2, 3], 'three', two=2)