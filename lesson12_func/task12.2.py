date = {'login': "log",
        'password' : 'pass',
        'old' : 15,
        'height': 185}
a = input('Какой параметр показать: ')
try:
        print(date[a])
except:
        print('Такого параметра нет')