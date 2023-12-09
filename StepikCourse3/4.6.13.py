import pickle
import sys

lines = []

for line in sys.stdin:
    lines.append(line.strip())

file_name = lines.pop(0)

with open(file_name, 'rb') as file:
    _func_name = pickle.load(file)

    print(_func_name(*lines))
