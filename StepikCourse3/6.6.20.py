from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values:
        sorted_keys = [i[0] for i in sorted(ordered_dict.items(), key=lambda pair: pair[1])]
        for key in sorted_keys:
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
