def palindromes():
    counter = 0
    while True:
        counter += 1
        if str(counter) == str(counter)[::-1]:
            yield counter
        else:
            continue
