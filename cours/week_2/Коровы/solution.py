# Коровы

k = int(input())
n = k
if n > 20:
    n = n % 10
if n == 1:
    print(k, 'korova')
elif n > 1 and n <= 4:
    print(k, 'korovy')
elif n == 0 or (n >= 5 and n <= 20):
    print(k, 'korov')
else:
    print('Не верное число коров')
