num = input('Введите номер: ')

while not (len(num) > 6 and num[0] == '+' and num[1:].isdigit()):
    print("Оибка")
    num = input("Введите номер: ")
print('Все ОК')
