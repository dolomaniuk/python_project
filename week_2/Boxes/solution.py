a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())


def sorting(a, b, c):
    while (a < b) or (b < c):
        if a < b:
            a, b = b, a
        if b < c:
            b, c = c, b
    return a, b, c


a1, b1, c1 = sorting(a1, b1, c1)
a2, b2, c2 = sorting(a2, b2, c2)

if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a1 >= a2 and b1 >= c2 and c1 >= b2:
    print('The first box is larger than the second one')
elif a1 >= b2 and b1 >= c2 and c1 >= a2:
    print('The first box is larger than the second one')
else:
    print('The first box is smaller than the second one')
