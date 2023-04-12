import turtle

turtle.setup(600,600) #создает поле 600*600 пикселей
turtle.shape("turtle") #вид черепашки
turtle.up() #поднимает перо


turtle.goto(-200,-200) #идет в конкретную точку с координатами
turtle.down() #опускает перо
for i in range (74):
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

turtle.up() #поднимает перо
turtle.goto(150,150)
turtle.dot (150, "orange")
turtle.right(135)

turtle.goto(-290,-290)

turtle.color("green")
turtle.pensize(3) #толщина линии
for i in range(28):
    turtle.down()
    turtle.right(10)
    turtle.forward(50)
    turtle.right(25)
    turtle.forward(20)
    turtle.left(35)
    turtle.up()  # поднимает перо
    turtle.sety(-290)

turtle.mainloop() #отображает результат пишется в конце

