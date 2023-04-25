import turtle

turtle.setup(600,600) #создает поле 600*600 пикселей
turtle.shape("turtle") #вид черепашки
turtle.dot (50, "red") #нарисовать закрашенный круг

turtle.up() #поднимает перо

turtle.goto(-150,150) #идет в конкретную точку c координатами

turtle.down() #опускает перо


turtle.pensize(5) #толщина линии
turtle.right(90) #поворот на права
turtle.forward(100) #передвинутся на 100 пикселей прямо

turtle.clear() #стереть все c экрана

turtle.color("red") #меняет цвет пера

turtle.left(45) #поворот налево
turtle.forward(150)

turtle.circle(50, 360) #рисует окружность

turtle.reset() #очищает экран и ставит черепаху в середину

turtle.mainloop() #отображает результат пишется в конце