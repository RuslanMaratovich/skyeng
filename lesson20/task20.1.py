from bs4 import BeautifulSoup


with open('index.html', encoding='utf8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

t = soup.title.text

print(t)

r = soup.find('div', class_='top_block') #получаем все из класса top_block
print(r)

d = soup.find('div', class_='header_right').text #получаем текст из класса header_right
print(d)

e = soup.find('div', class_='top_block').find('h2').text
print(e)