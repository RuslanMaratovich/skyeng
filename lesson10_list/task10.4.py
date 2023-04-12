import random
import turtle

color = []  # список цветов
a = ''
while a != 'exit':
    a = input('Введите цвет на английском: ')
    if a != 'exit':
        color.append(a)
print('Список цветов:')
print(color)  # выводим цвета

x = -300  # начальные координаты
y = -100

turtle.shape("turtle") #вид черепашки
turtle.up()
turtle.goto(x, y)
turtle.down() #опускает перо
turtle.pensize(3) #толщина линии

for i in range(10): #делаем 10 квадратов
    random_index = random.randint(0, len(color) - 1)
    turtle.color(color[random_index])
    turtle.down()  # опускает перо
    for k in range (4):
        turtle.forward(50)
        turtle.left(90)
    turtle.up()
    x=x+70
    y=y+25
    turtle.goto(x,y)
turtle.mainloop()

#orange
# green
# red
# blue
# violet
# black
# blue
# exit