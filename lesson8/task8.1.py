# сумму всех чисел от 1 до number, которые кратны 3

namber = int(input('Введите число: '))
s = 0
for i in range(1, namber + 1):
    if i % 3 == 0:
        s = s + i

print('сумма: ', s)
