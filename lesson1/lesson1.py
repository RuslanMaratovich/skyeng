print("Hello world 'разные кавычки'")

print('Hello, friend')
print('Hi', 'Look at here!')
print("5" + "34")
print(5 + 34)
print(12, 34, 56)
print(12, 34, 56, sep="")
print(12, 34, 56, sep="💙")  # добавляет разделитель между символами
print('You are cool', end='! ')  # добавляет в конец фразы !  следующая строка начинается с этой же строки
print('Exactly')


name = "имя"  # переменная Sting
print(name)

namber = 20  # переменная int
print(namber)


# Спецсимволы
print("перенос на новую строку \n"
      "символ табуляции \t при нажатии таб ")



print("Математические операции")

# Сложение: +
# Вычитание: -
# Умножение: *
# Деление: /
# Целочисленное деление: //
# Остаток от деления: %
# Возведение в степень: **

print(15 // 10)
print(15 % 10)
print(21 // 4)
print(21 % 4)



a = "10"
b = "15"
d = a + b
a = b
t = a + d
'print(t, "\n")'




print("Задача 1")
film = "Человек-чебурек"
time = "17:00"
cinema = "Подвал"
print("Билет на '" + film + "' в " + time + " в кинотеатр '" + cinema + "' забронирован.")
print("Билет на '", film, "' в ", time, " в кинотеатр '", cinema, "' забронирован.", sep="")

print("\n ДЗ \n Задача 1")
print(2 ** 10)

print("\n ДЗ \n Задача 2")
print(7 * 24 * 60 * 60)

print("\n ДЗ \n Задача 3")
print((7 + 10) / 2)

print("\n ДЗ \n Задача 4")
side1 = 10
side2 = 5
p = (side1 + side2) * 2
s = side1 * side2
print("Ответ: P = ", p, "\nОтвет: S = ", s)
