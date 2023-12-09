import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        lines = list(csv.reader(csv_file))
        keys = lines.pop(0)
        column_values_dict = {}

        for key in keys:
            fields = []
            for column in lines:
                fields.append(column.pop(0))
            column_values_dict.setdefault(key, fields)

        return column_values_dict
