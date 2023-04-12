string = input('Введите строку: ')
for i in string: #проходимся по всем символом строки
    if i.isupper(): #True если сивол имеет верхий регистр
        print(i, end="")

