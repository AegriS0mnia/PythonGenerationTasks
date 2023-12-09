number: int = int(input())
numbers: tuple[int] = tuple(i for i in range(1, number + 1))
sums_of_digits: set[int] = {sum(map(int, list(str(num)))) for num in numbers}
result = []

for _sum in sums_of_digits:
    group = []
    for num in numbers:
        if sum(map(int, list(str(num)))) == _sum:
            group.append(num)
    result.append(len(group))

print(max(result, default=0))