'''Рисует 4 шестиугольника из 1 точки'''

import turtle
turtle.setup(600,600) #создает поле 600*600 пикселей
turtle.pensize(5) #толщина линии
for i in range(4):
    for i in range(6):
        turtle.forward(100) #передвинутся на 100 пикселей прямо
        turtle.left(60) #поворот налево
    turtle.right(90)  # поворот на права


turtle.mainloop() #отображает результат пишется в конце