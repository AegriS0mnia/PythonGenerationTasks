def nonempty_lines(file):
    with open(file, encoding='utf-8') as filename:
        lines = (i.rstrip() for i in filename if not(i.isspace()))
        for i in lines:
            if len(i) <= 25:
                yield i
            else:
                yield '...'
        