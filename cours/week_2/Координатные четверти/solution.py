#   Координаты четверти
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def ploskost(k, n):
    if k > 0 and n > 0:
        qadrans = '1'
    elif k < 0 and n > 0:
        qadrans = '2'
    elif k < 0 and n < 0:
        qadrans = '3'
    elif k > 0 and n < 0:
        qadrans = '4'
    else:
        qadrans = 0
        print('Четверть не определена')
    return qadrans

pl1 = ploskost(x1, y1)
pl2 = ploskost(x2, y2)

if pl2 == pl1:
    print('YES')
else:
    print('NO')
