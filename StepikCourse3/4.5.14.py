from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    print(len([i for i in zip_file.namelist() if '.' in i]))
