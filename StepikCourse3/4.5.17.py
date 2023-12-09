from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook (2).zip') as zip_file:
    info = zip_file.infolist()
    special_date = datetime(2021, 11, 30, 14, 22)
    chosen = sorted(
        [(i.filename.split('/')[-1], str(datetime(*i.date_time)), i.file_size, i.compress_size) for i in info if not (i.is_dir())])

    for i in chosen:
        if i != chosen[-1]:
            print(f'''{i[0]}
  Дата модификации файла: {i[1]}
  Объем исходного файла: {i[2]} байт(а)
  Объем сжатого файла: {i[3]} байт(а)''')
            print()
        else:
            print(f'''{i[0]}
  Дата модификации файла: {i[1]}
  Объем исходного файла: {i[2]} байт(а)
  Объем сжатого файла: {i[3]} байт(а)''', end='')
