from zipfile import ZipFile


def get_size(size):
    if size == 0:
        return ''
    elif size <= 2 ** 10:
        return f' {size} B'
    elif 2 ** 10 < size <= 2 ** 20:
        return f' {round(size / 2 ** 10)} KB'
    elif 2 ** 20 < size <= 2 ** 30:
        return f' {round(size / 2 ** 20)} MB'
    else:
        return f' {round(size / 2 ** 20)} GB'


with ZipFile('test .zip') as zip_file:
    info = zip_file.infolist()
    for i in info:
        print(i.filename)
    file_attributes = []
    for file in info:
        size = file.file_size if not (file.is_dir()) else 0

        if file.is_dir():
            indent = file.filename.count('/') - 1
            if file.filename.count('/') == 1:
                name = file.filename[:file.filename.find('/')]
            else:
                name = file.filename.split('/')[-2]
        else:
            indent = file.filename.count('/')
            name = file.filename.split('/')[-1]

        file_attributes.append((name, indent, get_size(size)))

    for file in file_attributes:
        print(f'{"  " * file[1]}{file[0]}{file[2]}')
