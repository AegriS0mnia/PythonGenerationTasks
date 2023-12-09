from zipfile import ZipFile

with ZipFile('4.5.15.zip') as zip_file:
    info = zip_file.infolist()

    total_size = sum([i.file_size for i in info])
    compressed_total_size = sum([i.compress_size for i in info])

    print(f'Объём исходных файлов: {total_size} байт(а)')
    print(f'Объём сжатых файлов: {compressed_total_size} байт(а)')
