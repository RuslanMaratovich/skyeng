'''программа проверяет правильность введенного номера'''

num = input('Введите номер: ')

while not (len(num) > 6 and num[1:].isdigit() and (num[0:2] == '+7' or num[0] == '8')):
    print("Оибка")
    num = input("Введите номер: ")
print('Все ОК')