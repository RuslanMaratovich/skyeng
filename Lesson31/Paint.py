from tkinter import *
from tkinter.colorchooser import askcolor  # зависимость для выбора цвета


class Paint:
    def __init__(self):  # Конструктор класса который создает наш редактор
        self.root = Tk()
        # добавить кнопку pen_button 'Ручка', которая вызывает метод .use_pen
        self.pen_button = Button(self.root, text='Ручка', command=self.use_pen)
        # расположение кнопки pen_button в окне
        self.pen_button.grid(row=0, column=0)

        # добавить кнопку brush_button 'Кисть', которая вызывает метод .use_brush
        self.brush_button = Button(self.root, text='Кисть', command=self.use_brush)
        # расположение кнопки brush_button в окне
        self.brush_button.grid(row=0, column=1)

        # добавить кнопку выбора цвета color_button 'Цвет', которая вызывает метод .choose_color
        self.color_button = Button(self.root, text='Цвет', command=self.choose_color)
        # расположение кнопки color_button в окне
        self.color_button.grid(row=0, column=2)

        # добавить кнопку eraser_button 'Ластик', которая вызывает метод .erase_button
        self.eraser_button = Button(self.root, text='Ластик', command=self.erase_button)
        # расположение кнопки color_button в окне
        self.eraser_button.grid(row=0, column=3)

        # добавить слайдер который меняет значение в диапазоне
        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        # расположение слайдера choose_size_button в окне
        self.choose_size_button.grid(row=0, column=4)
        # set устанавливает начальное значение для слайдера choose_size_button
        self.choose_size_button.set(5)

        self.can = Canvas(self.root, bg='white', width=1000, height=1000)  # данные холста
        self.can.grid(row=1, columnspan=5)

        self.setup()  # Метод задает начальные значения переменных в программе
        self.root.mainloop()  # безконечная отрисовка окна

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.eraser_on = False
        self.various = ROUND
        self.color = 'black'  # текущий цвет пера
        self.active_button = self.pen_button  # активная кнопка
        self.can.bind('<B1-Motion>',
                      self.paint)  # событие срабатывает когда нажимаем на B1 левую клавишу миши и двигаем ей по экрану
        # При возникновении событии вызывается метод .paint
        self.can.bind('<ButtonRelease-1>',
                      self.reset)  # событие отпускания левой кнопки мыши которое вызывает метод .reset

    def use_pen(self):
        self.activate_button(self.pen_button)  # для кнопки pen_button вызываем метод activate_button
        self.various = ROUND

    def use_brush(self):
        self.activate_button(self.brush_button)  # для кнопки brush_button вызываем метод activate_button
        self.various = BUTT

    def choose_color(self):
        self.color = askcolor()[1]  # функция открывает цветовую палитру и возвращает кортедж записи цвеци в 2- форматов
        # [1] шеснадцетеричный формат

    def activate_button(self, some_button, eraser_mode=False):  # Метод активации кнопки
        self.active_button.config(relief=RAISED)  # Сброс нажатия кнопки active_button
        some_button.config(relief=SUNKEN)  # эффект нажатия переданной кнопки
        self.active_button = some_button  # в переменную active_button передаем текущую нажатую кнопку
        self.eraser_on = eraser_mode

    def erase_button(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def reset(self, event):  # метод срабатывает во время события event
        self.old_x = self.old_y = None

    def paint(self, event):  # метод срабатывает во время события event
        # print(f'x: {event.x}, y: {event.y}')
        self.line_widt = self.choose_size_button.get()  # .get() получает текуще значение тощины линии у .choose_size_button

        self.paint_color = 'white' if self.eraser_on else self.color

        if self.old_x and self.old_y:
            # метод рисует линию от начальных координат до конечных с заданной толщиной
            self.can.create_line(self.old_x,
                                 self.old_y,
                                 event.x,
                                 event.y,
                                 width=self.line_widt,
                                 fill=self.paint_color,
                                 capstyle=self.various,
                                 smooth=True)

        self.old_x = event.x  # обнавляе значение X в переменной old_x
        self.old_y = event.y  # обнавляе значение y в переменной old_y


if __name__ == '__main__':
    Paint()
