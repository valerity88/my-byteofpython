import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имен, содержащих пробелы, необходимо использовать
# двойные ковычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'G:\\Backup' # Поставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в осовном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Создаем каталог, если его ещее нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)

# Имя zip-файла
target = today+ os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command =  "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
