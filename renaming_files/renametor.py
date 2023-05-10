import shutil, os, re

# Регулярное выражение по которому будет поиск имен
# с американскими датами (ММ-ДД-ГГГГ)
date_pattern = re.compile(r'''^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
''', re.VERBOSE)

# цикл по файлам в текущем каталоге
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    # пропуск ненужных файлов
    if mo == None:
        continue
    # получение отдельных фрагментов имен файлов
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)

# создание имен с европейской датой (ДД-ММ-ГГГГ)
ru_filename = before + day + '-' + month + '-' + year + after

#получение путей к файлам
work_dir = os.path.abspath('.')
amer_filename = os.path.join(work_dir, amer_filename)
ru_filename = os.path.join(work_dir, ru_filename)

# переименование файлов
print(f'Заменяем {amer_filename} на {ru_filename}...')
#shutil.move(amer_filename, ru_filename) РАСКОММЕНТИРОВАТЬ ПОСЛЕ ПРОВЕРКИ