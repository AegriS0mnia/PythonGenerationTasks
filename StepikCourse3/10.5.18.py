def reverse(sequence):
    for i in range(len(sequence)):
        yield sequence[-i - 1]
