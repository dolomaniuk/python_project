def sum(summa):
    n = int(input())
    if n != 0:
        summa = sum(summa) + n
    return summa


print(sum(0))
