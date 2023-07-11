from tkinter import *


class Paint:
    def __init__(self):
        self.root = Tk()
        self.pen_button = Button(self.root, text='Ручка', command=self.use_pen)  # свойства кнопки
        self.pen_button.grid(row=0, column=0)  # местоположение кнопки

        self.can = Canvas(self.root, bg='white', width=600, height=600)  # холст
        self.can.grid(row=1, column=0)
        self.setup()
        self.root.mainloop()  # безконечная отрисовка окна

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = 'black'
        self.active_button = self.pen_button

    def use_pen(self):
        print('кнопка нажата')
        self.activate_button(self.pen_button)

    def activate_button(self, some_button):
        some_button.config(relief=SUNKEN)
        self.active_button = some_button


if __name__ == '__main__':
    Paint()
