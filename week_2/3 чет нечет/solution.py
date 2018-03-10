a = int(input())
b = int(input())
c = int(input())

priznak = 0
summa = 0


def even(x):
    if x % 2 == 0:
        priznak = 0
    else:
        priznak = 1
    return priznak


summa = even(a) + even(b) + even(c)
if summa == 0 or summa == 3:
    print('NO')
else:
    print('YES')
