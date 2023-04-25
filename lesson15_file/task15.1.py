# r - чтение из файла
# w - для записи (н.ф)
# w+ - для чтения и записи (н.ф)
# a - дозаписать в файл (н.ф)

# различные кодировки
codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8"]

file = open('testsefgtse.txt', 'w+', encoding="utf-8") #создаст файл если нет

file = open('test.txt', 'r', encoding="utf-8")

a = file.read()  # читает весь документ
file.seek(0)

b = file.read(10)  # первые 10 символов
file.seek(2)  # переместиться на 10 символ

c = file.read(10)  # читаем 10 символов от текущего положения

d = file.readlines() #считать строку 3


file.close()  # закрыть документ

print(a)
print(b)
print(c)
print(d)

for i in d:
    print(i)
# breakpoint()
