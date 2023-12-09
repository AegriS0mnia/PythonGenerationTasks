from zipfile import ZipFile
from decimal import Decimal as D

with ZipFile('4.5.15.zip') as zip_file:
    info = zip_file.infolist()

    file_name_and_compress = [(i.filename, (D(i.compress_size) / D(i.file_size)) * 100) for i in info if
                              not (i.is_dir())]

    min_compress = min(file_name_and_compress, key=lambda x: x[1])[0].split('/')[-1]

    print(min_compress)
