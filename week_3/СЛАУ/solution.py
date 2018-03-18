a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


def sokrasheniu(l, m, n):
    m /= l
    n /= l
    l /= l
    return int(l), m, n


while (a != 1) or (c != 1):
    if a == 1:
        varzero = -c / a
        c += varzero * a
        d += varzero * b
        f += varzero * e
        # print('varzero', varzero, 'c=', c, 'd=', d, 'f=', f)
        y = f / d
        x = e - (b * y)
        break
    elif c == 1:
        varzero = -a / c
        a += varzero * c
        b += varzero * d
        e += varzero * f
        # print('varzero=', varzero, 'a=', a, 'b=', b, 'e=', e)
        y = e / b
        x = f - (d * y)
        break
    else:
        if a > c:
            a, b, e = sokrasheniu(a, b, e)
            # print('1)', a, b, c)
        else:
            c, d, f = sokrasheniu(c, d, f)
            # print('2)', c, d, f)

print(x, y)
