from bs4 import BeautifulSoup
import requests

url = 'https://job.skyeng.ru/programm-prepodavateli?utm_source=skysmart.ru_cc&utm_medium=landing&_ga=2.16319230.918013776.1687791981-173397605.1633021772&_gl=1*ny767t*_ga*MTczMzk3NjA1LjE2MzMwMjE3NzI.*_ga_K9WK84VK5J*MTY4Nzc5NDQ1OC42LjAuMTY4Nzc5NDQ2MS4wLjAuMA..*_ga_5DWC4JK87M*MTY4Nzc5NDQ1OC42LjAuMTY4Nzc5NDQ2MS41Ny4wLjA.#!/tab/407389345-3'

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36'}

r = requests.get(url, headers=head)  # делаем гет запрос к URL
src = r.text  # Записываем код сайта в переменную src

# Парсим src и передаем значения в soup
soup = BeautifulSoup(src, 'lxml')

# ищем значения класса в переменной soup
t = soup.find(class_="t958__author-name t-heading t-heading_xs").text
print(t)

# #ищем значения класса в переменной soup
# t = soup.find_all(class_="teacher-name ng-star-inserted")
# for i in t:
#     print(i.text)
