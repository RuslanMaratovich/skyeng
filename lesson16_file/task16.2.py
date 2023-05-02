'''программа считывает строки и выводит информацию по завершению'''

try:
    file = open('file.txt', 'r', encoding="utf-8")

    for line in file:
        print(line[:-1])
    print('файл считали')
except:
    print('Фаил не найден')