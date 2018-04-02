a = float(input())
n = int(input())


def power(a, n):
    if n != 0:
        if n % 2 == 0:
            return power((a * a), (n / 2))
        else:
            return a * power(a, n - 1)
    else:
        return 1


print(power(a, n))
