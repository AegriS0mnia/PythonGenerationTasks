def translate_to_bytes(coefficient: int, size: str) -> int:
    if size == 'KB':
        return coefficient * 2**10
    if size == 'MB':
        return coefficient * 2**20
    if size == 'GB':
        return coefficient * 2**30
    return coefficient


def get_size(size: int) -> str:
    if size <= 2 ** 10:
        return f' {size} B'
    elif 2 ** 10 < size <= 2 ** 20:
        return f' {round(size / 2 ** 10)} KB'
    elif 2 ** 20 < size <= 2 ** 30:
        return f' {round(size / 2 ** 20)} MB'
    else:
        return f' {round(size / 2 ** 30)} GB'

groups = []

with open('files.txt', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    files_extensions = sorted({f".{filename.split()[0].split('.')[1]}" for filename in lines})
    for file_extension in files_extensions:
        temp_group = []
        size_in_bytes = 0
        for line in lines:
            if file_extension in line:
                _line = line.split()
                size_in_bytes += translate_to_bytes(int(_line[1]), _line[2])
                temp_group.append(_line[0])
        overall_size = get_size(size_in_bytes)
        groups.append([sorted(temp_group), overall_size])

for group in groups:
     print(*group[0], sep='\n')
     print('----------')
     print(f'Summary:{group[1]}')
     print()
