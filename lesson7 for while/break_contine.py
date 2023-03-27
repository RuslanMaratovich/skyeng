for i in range(20):
    print(i)
    if i == 10:
        break
print('конец')

for i in range(20):
    if i%2 == 1:
        continue
    print(i)
print('конец')