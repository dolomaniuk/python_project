from math import sqrt
a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - (4 * a * c)
if D > 0:
    maxX = (-b + sqrt(D)) / (2 * a)
    minX = (-b - sqrt(D)) / (2 * a)
    print(minX, maxX)
elif D == 0:
    x = (-b + sqrt(D)) / (2 * a)
    print(x)
