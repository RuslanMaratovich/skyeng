import turtle
import random

colors = ['green', 'red', 'blue', 'black', 'aqua', 'pink']

x = -400
y = -200

turtle.shape("turtle") #вид черепашки
turtle.up()

for i in range(15):
    turtle.goto(x, y)
    random_index = random.randint(0, len(colors) - 1)
    random_color = colors[random_index]
    turtle.dot(50, random_color)
    y = y + 25
    x = x + 50

turtle.mainloop()