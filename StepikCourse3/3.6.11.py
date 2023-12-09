import time


def get_the_fastest_func(funcs, arg):
    func_and_time = []

    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        elapsed_time = end - start
        func_and_time.append((elapsed_time, func))

    fastest_func = min(func_and_time)[1]

    return fastest_func
