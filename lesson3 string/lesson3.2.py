"""ДЗ задача 4 подсчет цифр в строке"""

str4 = input('введите строку: ')
sr4 = str4.count('0')+str4.count('1')\
      +str4.count('2')+str4.count('3')\
      +str4.count('4')+str4.count('5')\
      +str4.count('6')+str4.count('7')\
      +str4.count('8')+str4.count('9')
print('\nколличество цифр в строке',str4, sr4)

# \ перенос на следующую строку