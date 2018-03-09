"""
Определить максимум в последовательности натуральных чисел, конец = 0
"""
# n = int(input())
max1 = 0
max2 = 0
n = -1
while n != 0:
    n = int(input())
    if n > max1:
        max2 = max1
        # print('max2', max2)
        max1 = n
        # print('max1:', max1)
    elif n > max2:
        max2 = n
print(max2)
