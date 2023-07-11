class Human:
    name = ''
    country = ''
    Min_age = 0
    Max_age = 100

    @classmethod #Метод который привязан к классу, а не к атрибуту класса
    def validate(cls, age):
        return cls.Min_age <= age <= cls.Max_age

    def __init__(self, age, name, country):  # Конструктор
        print('Work')
        self.age = 0
        self.name = 'Empty'
        self.country = 'Empty'
        if Human.validate(age):
            self.age = age
            self.name = name
            self.country = country

    @staticmethod #Статический метод
    def norm(height, weight):
        return (height - weight)

    def data(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def data2(self):
        return (self.age, self.name, self.country)


print(Human.validate(500))

h1 = Human(33, 'Руслан', "Россия")
h2 = Human(200, 'Саша', "Индия")
# h1.data(33, 'Руслан', "Россия")
print(h1.__dict__)
print(h2.__dict__)

print(Human.norm(180, 75))
