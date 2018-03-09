n = int(input())
max1 = n
if n != 0:
    i = 1   # count
else:
    i = 0
while n != 0:
    n = int(input())
    if n > max1:
        i = 1
        max1 = n
        # print('max1:', max1)
    elif n == max1:
        i += 1
        # print('i:', i)
print(i)
