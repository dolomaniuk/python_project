from math import sqrt

a = float(input())
b = float(input())
c = float(input())

p = (1 / 2) * (a + b + c)
s = sqrt(p * (p - a) * (p - b) * (p - c))
# print('{0:.6f}'.format(s))
print(s)
