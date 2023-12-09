def simple_sequence():
    begin = 1
    while True:
        for i in range(begin):
            yield begin
        begin += 1
