text = input().split()

lengths = [len(i) for i in text]
groups = []
for length in lengths:
    count = 0
    for i in text:
        if len(i) == length:
            count += 1
    local_group = (length, count)
    if local_group not in groups:
        groups.append(local_group)

    groups.sort(key=lambda el: el[1])

for i in groups:
    print(f'Слов длины {i[0]}: {i[1]}')

