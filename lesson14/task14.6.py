import turtle

def create_dot(color, x, y, r):
    flag = False
    turtle.up()
    try:
        turtle.goto(int(x), int(y))
    except:
        print('Ошибка перехода в координаты')
        flag = True

    turtle.down()

    try:
        turtle.dot(int(r), color)
    except:
        print('Ошибка рисования')
        flag = True
    return flag



turtle.pensize(3)
flag = True

while flag:
    color = input('Введите цвет: ')
    x = input('Введите X: ')
    y = input('Введите Y: ')
    r = input('Введите R: ')
    flag = create_dot(color, x, y, r)

turtle.mainloop()

