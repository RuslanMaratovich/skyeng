from bs4 import BeautifulSoup


with open('index.html', encoding='utf8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

t = soup.title.text

r = soup.find('h1') #находит первый тег h1

c = soup.find_all('h1') #находит все теги h1 и помещает их в список

print(t)
print(r)
print('\n',c)