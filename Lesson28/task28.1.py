'''инкапсуляция ограничения доступа'''


# attribute (без подчеркиваний) - публичное свойство (public)

# _attribute (с 1 подчеркиванием) -режим доступа protected
# (Служит для обращения внутри класса и во всех его дочерних классках)

# __attribute (с 2 подчеркиванием) - режим доступа private
# (служит для обращения только внутри класса)

class Location:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check(cls, x, y):
        return type(x) in (int, float) and type(y) in (int, float)

    def set_coord(self, x, y):  # сетр передает значения в программу
        if self.__check(x, y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('ВЫ ввели неправельные данные. Введите числа')

    def get_coord(self):  # гетр возвращает значения в программу
        return self.__x, self.__y


loc = Location(5, 6)
loc.set_coord("1", 5)
print(loc.get_coord())
