import zipfile, os

def backzip(folder):
    folder = os.path.abspath(folder)

    # определение имени файла от существующего
    num = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists((zip_filename)):
            break
        num += 1

    print(f'Создание архива {zip_filename}...')
    backupzip = zipfile.ZipFile(zip_filename, 'w')

    for foldname, subfol, filenames in os.walk(folder):
        print(f'Добавление файлов из папки {foldname}...')
        backupzip.write(foldname)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue #не создаем копий зип архивов

            backupzip.write(os.path.join(foldname, filename))
    backupzip.close()
    print('Архив создан.')


backzip('D:\\delicious')
