"""
Определить сумму последовательности натуральных чисел, конец = 0
"""

summa = 0
n = -1
while n != 0:
    n = int(input())
    if n == 0:
        break
    summa += n

print(summa)
