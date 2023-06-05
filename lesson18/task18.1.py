import requests

a = requests.get('https://skysmart.ru/')

print(a.status_code)

#a.status_code == 2XX - все хорошо, ответ пришел на наш запрос
#a.status_code == 3XX - сайт перенаправляет пользователя
#a.status_code == 4XX - ошибка на стороне пользователя
#a.status_code == 5XX - ошибка на стороне сайта

#a.status_code == True - запрос принят и ответ отправлен
#a.status_code == False - произошла ошибка и

if a.status_code == 200:
    print('Все хорошо')
    print(a.text)