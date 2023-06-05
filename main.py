import turtle
import random
#turtle.setup(500,500)
turtle.pensize(2)
colors = [ 'red',  'black', 'aqua', 'pink']
dlina =[""]
turtle.up()
turtle.goto(-200,0)
turtle.down()
turtle.left(90)
x = -200
for i in range(10):
    r = random.randint(0, len(colors) - 1)
    turtle.color(colors[r])
    t = random.randint(10,50)
    turtle.goto(x,200)
    x = x + t
    turtle.goto(x,0)
turtle.mainloop()