crdX1 = int(input())
crdY1 = int(input())
crdX2 = int(input())
crdY2 = int(input())
if crdX1 - 1 > 1:
    minX = crdX1 - 1
else:
    minX = 1
if crdY1 - 1 > 1:
    minY = crdY1 - 1
else:
    minY = 1
if crdX1 + 1 < 8:
    maxX = crdX1 + 1
else:
    maxX = 8
if crdY1 + 1 < 8:
    maxY = crdY1 + 1
else:
    maxY = 8

X2 = (crdX1 - 1) <= crdX2 <= (crdX1 + 1)
Y2 = (crdY1 - 1) <= crdY2 <= (crdY1 + 1)
if X2 and Y2:
    print('YES')
else:
    print('NO')
