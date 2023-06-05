import turtle
def domik():
    def quadro():
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
    def crish():
        turtle.forward(100)
        turtle.left(140)
        turtle.forward(80)
        turtle.left(92)
        turtle.forward(70)
    def okno():
        for i in range(4):
            turtle.forward(30)
            turtle.left(90)

    quadro()
    turtle.up()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.down()
    crish()
    turtle.left(128)


domik()
turtle.up()
turtle.goto(-150,0)
turtle.down()
domik()
turtle.up()
turtle.goto(150,0)
turtle.down()
domik()


turtle.exitonclick()