import turtle

x, y = 0, 0

x_list = []
y_list = []

while x != 'exit' and y != 'exit':
    x_list.append(int(x))
    y_list.append(int(y))
    x = input('Введите координаты Х: ')
    y = input('Введите координаты Y: ')


turtle.pensize(3) #толщина линии
for i in range(len(x_list)):
    turtle.goto(x_list[i], y_list[i])
    print(f'Перешли на х = {x_list[i]}, y = {y_list[i]}')

turtle.mainloop()