# Шашки


def isEven(m, n):   # доступность выполнения скрипта
    validate = 0
    if ((m + n) % 2 == 0) and (1 <= m <= 8) and (1 <= n <= 8):
        validate = 1
    return validate


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if isEven(x1, y1) and isEven(x2, y2):
    if abs(x2 - x1) <= (y2 - y1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
