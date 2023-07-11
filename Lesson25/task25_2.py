class Human:
    age = 0
    name = ''
    country = ''

    def data(self, age, name, country):
        self.age = age
        self.name = name
        self.country = country

    def data2(self):
        return (self.age, self.name, self.country)


h = Human()
