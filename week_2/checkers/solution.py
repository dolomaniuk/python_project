# Шашки


def isEven(m, n):   # доступность выполнения скрипта
    validate = 0
    if (1 <= m) and (m <= 8) and (1 <= n) and (n <= 8):
        if n % 2 != 0:
            if m % 2 != 0:
                validate = 1
        else:
            if m % 2 == 0:
                validate = 1
    return validate


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if isEven(x1, y1) and isEven(x2, y2):
    varX = x1
    varY = y1

    while varY < y2:
        varY += 1
        if x2 <= varX:
            if (varX - 1) >= 1:  # что бы не выйти за края
                varX -= 1
        else:
            if (varX + 1) <= 8:  # что бы не выйти за края
                varX += 1
        # print(varX, varY)
else:
    varX = -x2

if x2 == varX:
    print('YES')
else:
    print('NO')
