login = input('логин: ')
password = input('пароль: ')
email = input('Почта: ')
phone = input('Телефон: ')


if len(login) > 6 and len(password) > 6:
    print('Логин и пароль верны')
else:
    print('Логин и пароль не верны')
if '@' in email:
    print('почта верна')
else:
    print('Почта не верна')
if (phone[0:2] == '+7' or phone[0]== '8') and len(phone) > 10:
    print('телефон верный')
else:
    print('Телефон не верный')


