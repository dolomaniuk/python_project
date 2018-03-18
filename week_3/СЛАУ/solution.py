a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

if a == 1:
    varzero = -c / a
    c += varzero * a
    d += varzero * b
    f += varzero * e
    print('varzero', varzero, 'c', c, 'd', d)
    y = f / d
    x = e - (b * y)
    print('y', y, 'x', x)
elif c == 1:
    varzero = -a / c
    a += varzero * c
    b += varzero * d
    y = e / b
    x = f - (d * y)
else:
    a = 1
    b /= a
    e /= a
    varzero = -c / a
    c += varzero * a
    d += varzero * b
    y = f / d
    x = e - (b * y)

print(x, y)
    # ax + by = e
    # cx + dy = f

