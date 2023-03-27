userString = input('Введите строку: ')

leftBracket = userString.find('(')
rightBracket = userString.find(')')

print(userString[leftBracket+1: rightBracket])

