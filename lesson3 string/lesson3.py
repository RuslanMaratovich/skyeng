#строки


a = 10
b = 'привет '
print('a =', a)
print('a = ' + str(a))  # переводим int в str
print(b * 3 + '\n')  # выведет строку 3 раза

st = 'Привет, сегодня хорошая погода!'
print('исходная строка:', st)

print('.count(\'о\')', st.count('о'))  # .count - метот который показвает количество встречаемых аргументов в строке

print('.replece(\'сегодня\', \'завтра будет\')', st.replace('сегодня', 'завтра будет'))  # .replece - метот заменяет первый аргумент в строке вторым

print('len(str)', len(st))  # len(str) - функция подсчета символов в строке

print('.index(\'П\')', st.index('П'))  # .index() - метот показывает под каким индексом в первый раз встречается буква п от 0

print('.rindex(\'п\')', st.rindex('п'))  # .rindex() - метот показывает под каким индексом в первый раз встречается буква п c конца строки

print('подстрока [8:19]', st[8:19]) #вести строку от 8 индекса включительно до 19 индекса не включая его

print('подстрока [8:-5]', st[8:-5]) #вести строку от 8 индекса включительно до -5 индекса -5 ститает индексы c конца строки

print('.lower()', str.lower()) #.lower() - метод переводит все символы строки в нижний регистр

print('.upper()', str.upper()) #.lower() - метод переводит все символы строки в верхний регистр




#Задача 1
sr1 = input('\n введите строку для подсчета слов по пробелам: ')
print(sr1.count(' ') + 1)
print("Новая строка: " + sr1.replace(' ', ','))


#Задача 2
sr2 = 'Привет, я изучаю Python!'
print(sr2[0])
print(sr2[-24])
print(sr2[0:6])
print(sr2[-24:-18])
print(sr2[8:16])
print(sr2[-16:-8])
print(sr2[17])
print(sr2[-7])

#ДЗ задача 3 удаление пробелов в строке
sr3 = 'Я программирую на Python'
print('\n' + sr3.replace(' ', ''))
print('Тестовая строка один'.replace(' ', ''))
print('Это самый простой метод'.replace(' ', ''))

#ДЗ задача 4 подсчет цифр в строке
str4 = 'Пр20ив11е5т'
sr4 = str4.count('0')+str4.count('1')\
      +str4.count('2')+str4.count('3')\
      +str4.count('4')+str4.count('5')\
      +str4.count('6')+str4.count('7')\
      +str4.count('8')+str4.count('9')
print('\nколличество цифр в строке',str4, sr4)

# \ перенос на следующую строку