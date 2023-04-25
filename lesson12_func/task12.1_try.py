# NameError - Такое имя не найдено
# ArithmeticError - Арифметическая ошибка
# ValueError - Ошибка значения

try:
    a = float(input('Введите число: '))
    b = int(input('Введите число: '))
    d = a / b
except NameError:
    print('ошибка в имени')
except ValueError:
    print('ошибка ввода')
except ArithmeticError:
    print('ошибка в арифметике')
finally:
    print('Сработает в любом случа')


