class Human:
    age = 0
    name = ''
    country = ''

    def __init__(self, age, name, country):  # Конструктор
        print('Work')
        self.age = age
        self.name = name
        self.country = country

    def data(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def data2(self):
        return (self.age, self.name, self.country)


h1 = Human(33, 'Руслан', "Россия")
h2 = Human(21, 'Саша', "Индия")
# h1.data(33, 'Руслан', "Россия")
print(h1.__dict__)
print(h2.__dict__)