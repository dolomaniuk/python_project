from math import sqrt
a = float(input())
while a == 0:
    print('a have to be > 0. Input a:')
    a = int(input())
b = float(input())
c = float(input())

D = b ** 2 - (4 * a * c)
# print(D)
if D > 0:
    maxX = (-b + sqrt(D)) / (2 * a)
    minX = (-b - sqrt(D)) / (2 * a)
    print(minX, maxX)
elif D == 0:
    x = (-b + sqrt(D)) / (2 * a)
    print(x)
