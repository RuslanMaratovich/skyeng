'''подсчет колличества строк в файле'''
name = input('Введите имя файла: ')
try:
    file = open(name, 'r', encoding="utf-8")
    quantityStr = 0
    for i in file.readlines():
        quantityStr += 1
    file.close()
    print('В файле:', quantityStr, 'cтрок')
except:
    print('файл "'+ name + '" не найден')
