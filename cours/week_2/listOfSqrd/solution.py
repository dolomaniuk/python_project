"""
По данному целому числу N распечатайте все квадраты натуральных
чисел,не превосходящие N, в порядке возрастания
"""

N = int(input())
i = 1   # variable
while i <= N:
    if i ** 2 <= N:
        print(i ** 2, end=' ')
    i += 1
