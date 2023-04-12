for i in '123456789':
    print (i)
    if int(i)>5:
        break
else:
    print('Сработал блок Else')     #сработает если цикл дойдет до конца

print('Новый цикл')
for i in '123456789':
    print (i)
    if int(i)>10:
        break
else:
    print('Сработал блок Else')     #сработает если цикл дойдет до конца