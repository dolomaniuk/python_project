n = float(input())

summa = 0
i = 1
# 1+(1 / 2²)+(1 / 3²)+...+(1 / n²)
while i <= n:
    summa += 1 / (i ** 2)
    i += 1
print(summa)
