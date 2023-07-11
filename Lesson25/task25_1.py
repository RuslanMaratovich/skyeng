class Car:
    model = 'BMW'
    color = 'red'
    price = 14000

    def carpoint(self):
        print('метод carpoint'+ str(self))

    def carrealise(self, data, time):
        self.data = data
        self.time = time
        
