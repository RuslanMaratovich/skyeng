a = True
b = 0
print('1 - yes, 2 - no')
while a:
    print("ваше число", b, "?")
    z = input('Ответ: ')
    if z == '1': a = False
    if z == '2': b = b + 1
print('я угадал, это число', b)
