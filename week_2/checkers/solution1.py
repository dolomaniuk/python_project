# Шашки
import math
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

paramGO = 1  # доступность выполнения скрипта

if y2 <= y1:
    paramGO = 0
if y2 % 2 == 0:  # определяем, четность или нечетность для X в искомой строке
    isEven = 0
    print('even')
    paramGO = 1
else:
    isEven = 1
    print('odd')
    if x2 % 2 == 0:  # есть ли смысл продолжать,при нечетном Y д.б. четный X
        paramGO = 0


if paramGO == 1:
    maxDistX = int(math.fabs(y2 - y1))
    print('maxDistX', maxDistX)
    dostMinX = int(math.fabs(x1 - maxDistX))
    print('dostMinX', dostMinX)
    if x1 - maxDistX < 1:
        dostMinX = 1
    print('dostMinX', dostMinX, 'after')
    dostMaxX = x1 + maxDistX
    print('dostMaxX', dostMaxX)
    if dostMaxX > 8:
        dostMaxX = 8
    print('dostMaxX', dostMaxX, 'after')
    if dostMinX <= x2 <= dostMaxX:
        if isEven and x2 % 2 != 0:
            print('YES')
        elif isEven == 0 and x2 % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
