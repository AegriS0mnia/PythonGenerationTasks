def inversions(sequence):
    inversions = 0
    counter = 0
    for num in sequence:
        for i in range(counter + 1, len(sequence)):
            if num > sequence[i]:
                inversions += 1
        counter += 1
    return inversions
