line = eval(input())

if isinstance(line, list):
    print(line[-1])
elif isinstance(line, tuple):
    print(line[0])
else:
    print(len(line))