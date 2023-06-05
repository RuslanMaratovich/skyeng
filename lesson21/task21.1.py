from bs4 import BeautifulSoup
import requests

url = 'https://skysmart.ru/programmirovanie-dlya-detej/python'

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36'}

r = requests.get(url, headers = head) #делаем гет запрос к URL
src = r.text #Записываем код сайта в переменную src

#Открываем файл index.html и передаем в переменную f
#Записываем в файл информацию из src
with open('index.html', 'w', encoding='UTF8') as f:
    f.write(src)

#Открываем файл index.html и передаем в переменную f
#Считываем информацию из файла в переменную src
with open('index.html', encoding='UTF8') as f:
    src = f.read()

# Парсим src и передаем значения в soup
soup = BeautifulSoup(src, 'lxml')

#ищем значения класса в переменной soup
t = soup.find(class_="teacher-name ng-star-inserted").text
print(t)

#ищем значения класса в переменной soup
t = soup.find_all(class_="teacher-name ng-star-inserted")
for i in t:
    print(i.text)