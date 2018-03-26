x = float(input())
y = float(input())


def isInGap(a):
    if -1 <= a <= 1:
        return 'YES'
    return 'NO'


def IsPointInSquare(x, y):
    print(isInGap(x) and isInGap(y))


IsPointInSquare(x, y)
