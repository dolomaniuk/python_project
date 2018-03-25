from math import sqrt
a = float(input())
while a == 0:
    print('a have to be > 0. Input a:')
    a = int(input())
b = float(input())
c = float(input())

eps = 5 * 10 ** (-7)
D = b ** 2 - (4 * a * c)
# print(D)
if D > 0:
    X1 = (-b + sqrt(D)) / (2 * a)
    X2 = (-b - sqrt(D)) / (2 * a)
    if (X1 + eps) < X2: # проверка на большее число
        print(X1, X2)
    else:
        print(X2, X1)
elif D == 0:
    x = (-b + sqrt(D)) / (2 * a)
    print(x)
