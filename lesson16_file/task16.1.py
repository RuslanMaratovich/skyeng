'''пример работы с файлами и папками'''
import shutil
import os

# shutil.copy() - копирует файл
#
# shutil.move() - перемещает файл

# shutil.rmtree() - удаляет папку и вложенные файлы

# os.remove() - удаляет конечны файл

shutil.move(r'C:\Users\Ruslan\PycharmProjects\skyeng\lesson16_file\directory1\test.txt', 'C:\\Users\\Ruslan\\PycharmProjects\\skyeng\\lesson16_file\\directory2\\test.txt')
shutil.copy(r'C:\Users\Ruslan\PycharmProjects\skyeng\lesson16_file\directory2\test.txt', 'C:\\Users\\Ruslan\\PycharmProjects\\skyeng\\lesson16_file\\directory3\\test.txt')
os.remove(r'C:\Users\Ruslan\PycharmProjects\skyeng\lesson16_file\directory3\test.txt')
shutil.rmtree(r'C:\Users\Ruslan\PycharmProjects\skyeng\lesson16_file\directory3')