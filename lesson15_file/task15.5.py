'''программа сортирует массив и сохраняет его в файл'''
list = [654, 654, 89, 99, 5656, 1, 10]

list.sort()

file = open('sort.txt', 'w+', encoding="utf-8")

for i in list:
    file.write(str(i)+'\n')

file.close()