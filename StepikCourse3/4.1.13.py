import sys

heights = []

for line in sys.stdin:
    heights.append(int(line.strip()))

if heights:
    print(f"""Рост самого низкого ученика: {min(heights)}
Рост самого высокого ученика: {max(heights)}
Средний рост: {sum(heights) / len(heights)}""")
else:
    print("нет учеников")
