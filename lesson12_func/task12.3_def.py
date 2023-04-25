import turtle


def create_rect():
    for i in range(4):
        turtle.left(90)
        turtle.forward(100)


def create_tr():
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(170)
    turtle.left(90)


def create_circle():
    turtle.dot(50, "red")



turtle.pensize(3)

create_rect()
turtle.up() #поднимает перо
turtle.forward(40)
turtle.down()
create_tr()
turtle.up() #поднимает перо
turtle.forward(40)
turtle.down()
turtle.circle(120, 360)
turtle.mainloop()
