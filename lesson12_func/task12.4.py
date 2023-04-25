import turtle


def house():
    for i in range(74):
        turtle.left(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(1)

    turtle.left(90)
    turtle.forward(150)
    turtle.left(45)
    turtle.forward(105)
    turtle.left(90)
    turtle.forward(105)


house()

turtle.mainloop()
