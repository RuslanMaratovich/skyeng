def add_num():
    list = []
    c = ''
    while True:
        c = input('Ведите число: ')
        if c == 'exit':
            break
        try:
            list.append(int(c))
        except:
            print('Ошибка добавления числа')

    u = check(list)
    return u


def check(list):
    t = True
    for i in list:
        if i > 10:
            t = False
    return t


print(add_num())
