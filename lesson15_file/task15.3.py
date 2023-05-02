'''считывает строки в файле в диапазоне'''
name = input('Введите имя файла: ')
x = int(input('Введите номер начальной строки файла: '))
y = int(input('Введите номер конечной строки файла: '))


try:
    file = open(name, 'r', encoding="utf-8")
    list_text = []
    flag = 0
    for i in file.readlines():
        flag += 1
        if flag >= x and flag <= y:
            list_text.append(i[0:-1])

    file.close()
    print(list_text)
except:
    print('Фаил не найден')