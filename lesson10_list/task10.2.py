import turtle
import random

colors = ['green', 'red', 'blue', 'black', 'aqua', 'pink']

x = 0
y = 0

turtle.pensize(3)

for i in range(15):
    random_index = random.randint(0, len(colors) - 1)
    random_color = colors[random_index]
    turtle.color(random_color)
    turtle.down()
    turtle.forward(100)
    turtle.up()
    y = y + 10
    turtle.goto(x, y)

turtle.mainloop()