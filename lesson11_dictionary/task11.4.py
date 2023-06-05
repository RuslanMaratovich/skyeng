import turtle
import random

turtle.setup(500, 500)
turtle.up()
turtle.goto(-200, 0)
turtle.down()
turtle.pensize(3)
turtle.left(90)
col = ['red', 'green', 'aqua', 'pink']
for i in range(5):
    while True:
        k = turtle.position()
        if k[1] < 199:
            turtle.forward(1)
        else:
            break
    k = turtle.position()
    print(k)
    r = len(col) - 1
    l = random.randint(0, r)
    turtle.color(col[l])
    turtle.goto(k[0] + random.randint(1, 30), 0)
turtle.mainloop()
