import time

def calculate_it(func, *args):
    start = time.perf_counter()
    func_return = func(*args)
    end = time.perf_counter()

    elapsed_time = end - start

    return func_return, elapsed_time

