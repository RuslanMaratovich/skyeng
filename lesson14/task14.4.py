def parse(n, line, k):
    start = line.find(n)
    finish = line.find(k)
    s = line[start + len(n):finish]
    return s


line1 = input('Введите строку: ')
start1 = input('Начало поиска: ')
finish1 = input('Конец поиска: ')

print(parse(start1, line1, finish1))

