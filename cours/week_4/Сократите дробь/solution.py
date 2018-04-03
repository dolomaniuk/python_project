def ReduceFrnction(n, m):
    p = n / gcd(n, m)
    q = m / gcd(n, m)
    return print(int(p), int(q))


def gcd(n, m):
    while n != 0 and m != 0:
        if n > m:
            n = n % m
        else:
            m = m % n
    return n + m


n = int(input())
m = int(input())

ReduceFrnction(n, m)
