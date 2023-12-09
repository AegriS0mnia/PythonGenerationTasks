from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('temp.zip', mode='w') as temp_zip_file, ZipFile('files.zip', 'w') as zip_file:
    for file_name in file_names:
        temp_zip_file.write(file_name)

    info = temp_zip_file.infolist()
    files = [i.filename.split('/')[-1] for i in info if not (i.is_dir()) and i.file_size <= 100]
    for file in files:
        zip_file.write(file)
