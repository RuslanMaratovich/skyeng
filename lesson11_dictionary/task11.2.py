dog = {'порода': 'Хаски',
       'возраст': '2 года',
       'масса': '5 кг'}

while True:
    a = input('Что вывести: ')
    if a != 'exit':
        print(dog[a])
    else:
        break
