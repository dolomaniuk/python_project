from math import sqrt, pow
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def different(a, b):
    if a < b:
        x = b - a
    else:
        x = a - b
    return x


def distance(x1, y1, x2, y2):
    dist = sqrt(pow(different(x1, x2), 2) + pow(different(y1, y2), 2))
    return dist


print(distance(x1, y1, x2, y2))
