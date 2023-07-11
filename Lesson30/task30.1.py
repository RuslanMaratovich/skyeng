'''Полимофизм использование одного метода для разных классов'''

class Rectangle:

    def __init__(self, w, h):
        self.w = w

        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square:

    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle:

    def __init__(self, a, b, c):
        self.a = a

        self.b = b

        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)

r2 = Rectangle(1, 3)

s1 = Square(10)

s2 = Square(20)

t1 = Triangle(1, 2, 3)

t2 = Triangle(4, 5, 6)

box = [r1, r2, s1, s2, t1, t2]

for i in box:
    if isinstance(i, Rectangle):
        print(f'Прямоугольник {i.get_pr()}')
    else:
        print(f'другая фигура {i.get_pr()}')

# print (r1.get_rect_pr(), r2.get_rect_pr())

# print (s1.get_sq_pr(), s2.get_sq_pr())
