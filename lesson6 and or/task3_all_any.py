# all если верны все условия из списка
# any если верно хотябы одно условия из списка

login = input('логин: ')
password = input('пароль: ')
email = input('Почта: ')
phone = input('Телефон: ')

x = [len(login) > 6, len(password) > 6, '@' in email, phone[0: 2] == '+7' or phone[0] == '8']
if all(x):
    print('Все введено верно')
else:
    print('Где-то допущена ошибка')
