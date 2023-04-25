line =['строка 1', 'строка 2','строка 3','строка 4']
file = open('t_file.txt', 'w+', encoding="utf-8")

for i in line:
    file.write(i+'\n')
#file.writelines(line)

file.close()

line2 =['строка 5', 'строка 6','строка 7','строка 8']
file = open('t_file.txt', 'a', encoding="utf-8")

for i in line2:
    file.write(i+'\n')

file.close()

line3 =['строка 9', 'строка 10','строка 11','строка 12']
file = open('t_file.txt', 'a', encoding="utf-8")
file.writelines(line3)
file.close()