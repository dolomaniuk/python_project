"""
Определить максимум в последовательности натуральных чисел, конец = 0
"""
n = int(input())
max = n

while n != 0 and n < (10 ** 9):
    n = int(input())
    if n == 0:
        break
    if n > max:
        max = n

print(max)
