'''Наследование'''


class Human:
    name = 'Human'

    def Bio_data(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        # self.data()


class Biodata(Human):
    name = 'Andrey'
    def data(self):
        print('данные роста')


class Base_data(Human):

    def data(self):
        print('Внесение данных')


h = Human()
b = Biodata()
d = Base_data()

b.Bio_data(33, 173, 78)
d.Bio_data(33, 173, 78)

print(b.__dict__)
print(d.__dict__)

print(b.name)
print(d.name)