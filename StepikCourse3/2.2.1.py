d1, d2, d3 = 10, 20, 30

distance = 0


for i in range(3):
    min_dist = min(d1, d2, d3)

    if d1 == min_dist:
        d2 += min_dist
        d3 += min_dist
    if d2 == min_dist:
        d1 += min_dist
        d3 += min_dist
    if d3 == min_dist:
        d1 += min_dist
        d3 += min_dist

    distance += min_dist

print(distance)