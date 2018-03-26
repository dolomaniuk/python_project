x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
