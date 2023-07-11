'''абстракция'''


class PR:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr')


class Rectangle(PR):

    def __init__(self, w, h):
        self.w = w

        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(PR):

    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(PR):

    def __init__(self, a, b, c):
        self.a = a

        self.b = b

        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c


box = [Rectangle(1, 2), Rectangle(1, 3), Square(10),
       Square(20), Triangle(1, 2, 3), Triangle(4, 5, 6)]

for i in box:
    if isinstance(i, Rectangle):
        print(f'Прямоугольник {i.get_pr()}')
    else:
        print(f'другая фигура {i.get_pr()}')

