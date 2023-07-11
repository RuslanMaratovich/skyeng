class Human:

    def __init__(self, name):
        print('Ввод пользователя')
        self.name = name
        print('Объект обнаружен')

    def show (self):
        print('Привет, мое имя', self.name)

    def __del__(self): #метод del удаляет экземпляр класса
        print('Объект передан в деконструктор')
        print('Объект удален')

h1 = Human ('Иван')
h1.show()

# del h1
#
# h2 = Human ('Роман')
# h2.show()