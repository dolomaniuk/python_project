"""
Если С наибольшая сторона:

1) Если квадрат С равен сумме квадратов других сторон-- прямоугольный

2)Если квадрат С меньше суммы квадратов других сторон -- остроугольный

3)Если квадрат С больше суммы квадратов других сторон -- тупоугольный

любая сторона < суммы двух других сторон, иначе треугольник не существует
"""
a = int(input())
b = int(input())
c = int(input())

if (a < b + c) and (b < a + c) and (c < a + b):
    while a <= b or b <= c:
        if a < b:
            a, b = b, a
        if b < c:
            b, c = c, b
        # print(a, b, c)

    sum2 = (b ** 2) + (c ** 2)
    if a ** 2 == sum2:
        print('rectangular')
    elif a ** 2 < sum2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')
