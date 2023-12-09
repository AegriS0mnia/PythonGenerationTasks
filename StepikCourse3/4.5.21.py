from zipfile import ZipFile

def extract_this(zip_archive, *args):
    with ZipFile(zip_archive) as zip_file:
        infolist = zip_file.infolist()
        if not(args):
            zip_file.extractall()
        else:
            for file in infolist:
                file_name = file.filename.split('/')[-1]
                if not(file.is_dir()) and file_name in args:
                    zip_file.extract(file_name)
