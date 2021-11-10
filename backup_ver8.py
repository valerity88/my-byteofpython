import os
import time
import sys
import zipfile
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = input('Введите путь к файлу или каталогу, который требуется зарезервировать -->')
# Заметьте, что для имен, содержащих пробелы, необходимо использовать
# двойные ковычки внутри строки.
print(source)

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'G:\\Backup' # Поставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в осовном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Ввведите комментарий -->')
if len(comment) == 0: # прооверяем, введен ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip' 
 
# Создаем каталог, если его ещее нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив


# Запускаем создание резервной копии
newzip = zipfile.ZipFile(target, 'w')

for dirname, subdirs, files in os.walk(source): 
    print(dirname, subdirs, files)
    newzip.write(dirname)
    for file in files:
        newzip.write(os.path.join(dirname, file))
newzip.close()

print('Резервная копия успешно создана', target)


