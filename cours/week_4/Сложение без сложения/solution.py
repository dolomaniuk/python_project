a = int(input())
b = int(input())

summa = 0


def sum(a, b):

    if a > 0:
        return sum(a - 1, b) + 1
    if b > 0:
        return sum(a, b - 1) + 1
    return summa


print(sum(a, b))
