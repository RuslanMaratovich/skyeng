string = input('Введите строку: ')
for i in string: #проходимся по всем символом строки
    if i.islower(): #True если сивол имеет нижний регистр
        print(i, end="")
