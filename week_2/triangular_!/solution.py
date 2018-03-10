a = int(input())
b = int(input())
c = int(input())

while a < b or b < c:
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    # print(a, b, c)

sum2 = (b ** 2) + (c ** 2)

if (a < b + c) and (b < a + c) and (c < a + b):

    if a ** 2 == sum2:
        print('rectangular')
    elif a ** 2 < sum2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')
