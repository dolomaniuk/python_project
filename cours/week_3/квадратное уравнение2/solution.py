from math import sqrt
a = float(input())
b = float(input())
c = float(input())

varPas = 0
eps = 5 * 10 ** (-7)
D = b ** 2 - (4 * a * c)

if a == 0 and b != 0:
    x = -c / b
    print(f"1 {x:g}")    # 1 корень
    varPas = 1
elif a == b == c == 0:
    print(3)            # бесконечно много корней
    varPas = 1
elif a == b == 0 and c != 0:
    print(0)            # нет корней
    varPas = 1

# print(D)
if D > 0 and varPas != 1:
    X1 = (-b + sqrt(D)) / (2 * a)
    X2 = (-b - sqrt(D)) / (2 * a)
    if (X1 + eps) < X2:     # проверка на большее число
        print(f"2 {X1:g}", f"{X2:g}")
    else:
        print(f"2 {X2:g}", f"{X1:g}")
elif D == 0 and varPas != 1:
    x = (-b + sqrt(D)) / (2 * a)
    print(f"1 {x:g}")
elif D < 0 and varPas != 1:  # нет корней
    print(0)
