from math import sqrt, pow
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())


def different(a, b):
    if a < b:
        x = b - a
    else:
        x = a - b
    return x


def dist(a, b, c, d):
    dist = sqrt(pow(different(a, c), 2) + pow(different(b, d), 2))
    return dist


p = dist(x1, y1, x2, y2) + dist(x2, y2, x3, y3) + dist(x3, y3, x1, y1)

print(p)
