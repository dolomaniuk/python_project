a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

res = 0

if d >= e:
    maxW = d
    minW = e
else:
    maxW = e
    minW = d

while (a < b) or (b < c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b

if maxW >= a and minW >= b:
    res = 1
elif maxW >= a and minW >= c:
    res = 1
elif maxW >= b and minW >= c:
    res = 1

if res == 1:
    print('YES')
else:
    print('NO')
