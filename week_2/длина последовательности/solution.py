"""
Определить длину последовательности полож чисел, конец = 0
"""
length = 0
n = -1
while n != 0:
    n = int(input())
    if n < 0:
        continue
    elif n == 0:
        break
    else:
        length += 1

print(length)
