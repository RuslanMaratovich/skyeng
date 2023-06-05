import  turtle
turtle.setup(500,500)
turtle.forward(-150)
turtle.goto(-150,100)
turtle.goto(0,100)
turtle.goto(0,0)
x = 0
y = 0
for i in range(100):
    turtle.down()
    turtle.forward(-150)
    y = y + 1
    turtle.up()
    turtle.goto(x,y)


turtle.up()
turtle.goto(-150,100)
turtle.down()
turtle.goto(-70,150)
turtle.goto(-0,100)
turtle.up()
turtle.goto(200,170)
turtle.dot(150,"yellow")
turtle.goto(-250,-250)
turtle.down()
turtle.color("green")
turtle.mainloop()