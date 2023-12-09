def alternating_sequence(count=None):
    number = 1
    if count is None:
        while True:
            yield (-1)**(number % 2 + 1) * number
            number += 1
    else:
        for i in range(1, count + 1):
             yield (-1)**(i % 2 + 1) * i
