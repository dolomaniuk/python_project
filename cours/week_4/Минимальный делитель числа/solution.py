n = int(input())


def MinDivisor(n):
    i = 2
    while i <= n and n % i != 0:
            i += 1   # переход к следующему делителю
    else:    # в противном случае,
        return i     # выводится текущий делитель


print(MinDivisor(n))
