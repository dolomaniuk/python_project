a = float(input())
n = int(input())


def power(a, n):
    if n != 0:
        return a * power(a, n - 1)
    else:
        return 1


print(power(a, n))
