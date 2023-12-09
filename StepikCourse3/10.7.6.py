def parse_ranges(ranges):
    str_ranges = (i.split('-') for i in ranges.split(','))
    int_ranges = (tuple(map(int, i)) for i in str_ranges)
    ranges_ = (range(i[0], i[1] + 1) for i in int_ranges)
    for i in ranges_:
        yield from i
