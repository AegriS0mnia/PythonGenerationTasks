cache = {1: 1, 2: 1, 3: 1}

def tribonacci(number):
    result = cache.get(number)
    if result is None:
        result = tribonacci(number - 1) + tribonacci(number - 2) + tribonacci(number - 3)
        cache[number] = result
    return result

