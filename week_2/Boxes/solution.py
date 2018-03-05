'''
Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
что поворачивать коробки можно только на 90 градусов вокруг ребер
'''

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())


def sorting(a, b, c):       # сортируем в порядке убывания
    while (a < b) or (b < c):
        if a < b:
            a, b = b, a
        if b < c:
            b, c = c, b
    # print(a, b, c)
    return a, b, c


a1, b1, c1 = sorting(a1, b1, c1)
a2, b2, c2 = sorting(a2, b2, c2)

if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2:
    if b1 >= b2 and c1 >= c2:
        print('The first box is larger than the second one')
    else:
        print('Boxes are incomparable')
elif a1 <= a2:
    if b1 <= b2 and c1 <= c2:
        print('The first box is smaller than the second one')
    else:
        print('Boxes are incomparable')
else:
    print('Boxes are incomparable')
