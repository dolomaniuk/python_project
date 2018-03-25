# решение методом Крамера
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

delta = a * d - b * c
delX1 = e * d - b * f
delX2 = a * f - e * c

x1 = delX1 / delta
x2 = delX2 / delta

print(x1, x2)
