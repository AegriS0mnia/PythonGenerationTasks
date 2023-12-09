lines = input().split()

res = []
for line in lines:
    line = ''.join([i for i in line if i.isdigit() or i == '-'])
    line = line.split('-')

    if 4 <= len(line) <= 5:
        lengths = tuple([len(i) for i in line])
        first_pattern = line[0] == '7' and all(map(lambda l: l.isdigit(), line)) and lengths == (1, 3, 3, 2, 2)
        seconds_pattern = line[0] == '8' and all(map(lambda l: l.isdigit(), line)) and lengths == (1, 3, 4, 4)
        if first_pattern or seconds_pattern:
            res.append('-'.join(line))

print(*res, sep='\n')
