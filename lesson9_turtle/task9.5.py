import turtle
turtle.setup(600,600) #создает поле 600*600 пикселей
turtle.shape("turtle") #вид черепашки

for i in range (4):
    turtle.forward(50)
    turtle.left(90)

for i in range (50):
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

turtle.mainloop() #отображает результат пишется в конце