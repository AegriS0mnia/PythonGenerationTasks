def cyclic_shift(numbers: list[int | float], step: int) -> None:

    for i in range(abs(step)):
        if step > 0:
            numbers.insert(0, numbers[-1])
            del numbers[-1]
        else:
            numbers.append(numbers[0])
            del numbers[0]
