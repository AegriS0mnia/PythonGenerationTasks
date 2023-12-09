symbols = input()
line = input().lower()

letters = {}

for i in range(len(symbols)):
    letters.setdefault(chr(ord('a') + i), symbols[i])

for i in line:
    try:
        line = line.replace(i, letters[i])
    except:
        continue

print(line)
