# print('{0:.50f}'.format(0.1))
print(float(2**100).as_integer_ratio())
from math import floor, ceil, trunc
print(int(2.5), int(3.5), int(-2.5))
print(trunc(2.5), trunc(3.5), trunc(-2.5))
print(floor(2.5), floor(3.5), floor(-2.5))
print(ceil(2.5), ceil(3.5), ceil(-2.5))
print(round(2.5), round(3.5), round(-2.5))

s = 'abcd abc abd'
pos = s.find('abc')

while pos != -1:
    print(pos)
    pos = s.find('abc', pos + 1)

