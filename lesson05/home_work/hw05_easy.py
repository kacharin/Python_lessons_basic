# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

"""
import os

# Создаем
for i in range(1, 10):
    if os.path.exists("dir_" + str(i)) == False:
        os.mkdir("dir_" + str(i))
        print("Папка с названием dir_" + str(i) + " создана.")
    else:
        print("Папка dir_" + str(i) + " не создана, т.к. уже существует.")
print()

# Удаляем
for i in range(1, 10):
    if os.path.exists("dir_" + str(i)) == True:
        os.rmdir("dir_" + str(i))
        print("Папка с названием dir_" + str(i) + " удалена.")
    else:
        print("Папка dir_" + str(i) + " не удалена, т.к. не существует.")
"""

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

"""
import os

print('Папки в текущей директории:')

dirfile = os.listdir()

p = 0

for name in dirfile:
    if os.path.isdir(name) == True:
        p += 1
        print(name)

if p == 0:
    print('- в текущей директории папок не найдено.')
"""

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

"""

import os, shutil

runfile = os.path.basename(__file__)
print('Файл, из которого запущен данный скрипт:')
print(runfile)
print()

print('Копия файла, из которого запущен данный скрипт:')

runcopy = runfile + '.copy'

if os.path.isfile(runcopy) == False:
    shutil.copyfile(runfile, runcopy)
    print(runcopy)
else:
    print('- файл ' + runcopy + ' не создан, т.к. уже существует.')
"""
