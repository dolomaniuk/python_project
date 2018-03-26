from math import sqrt, pow
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def different(a, b):
    if a < b:
        x = b - a
    else:
        x = a - b
    return x


def IsPointInCircle(x, y, xc, yc, r):
    dist = sqrt(pow(different(x, xc), 2) + pow(different(y, yc), 2))
    return dist <= r


if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
