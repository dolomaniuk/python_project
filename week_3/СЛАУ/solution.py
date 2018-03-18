# решение методом Крамера
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

delta = a * d - b * c
delX1 = e * d - b * f
delX2 = a * f - e * c

x1 = delX1 / delta
x2 = delX2 / delta

print(x1, x2)
