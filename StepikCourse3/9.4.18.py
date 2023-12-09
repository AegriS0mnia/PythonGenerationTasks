def remove_marks(text, marks):
    cleared_text = ''.join([c for c in text if c not in marks])

    remove_marks.count += 1

    return cleared_text


remove_marks.count = 0
