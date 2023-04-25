# Пользователь вводит имена, и они сохраняются в списке.
# Список подаётся в функцию check().
# Функция check() возвращает новый список, в котором
# находятся имена, состоящие из более 5 символов.


def check(list):
    result = []
    for i in list:
        if len(i) > 5:
            result.append(i)
    return result


names = []
while True:
    c = input('Введите имя: ')
    if c.lower() == 'exit':
        break
    else:
        names.append(c)

print(check(names))
