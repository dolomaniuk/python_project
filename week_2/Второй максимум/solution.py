"""
Определить максимум в последовательности натуральных чисел, конец = 0
"""
n = int(input())
max1 = n
max2 = n

while n != 0:
    n = int(input())
    if n > max1 and max1 > max2:
        max1 = n
        print('max1:', max1)
    if max2 < n < max1:     #вычисляем второй максимум
        max2 = n
        print('max2:', max2)
print(max2)
