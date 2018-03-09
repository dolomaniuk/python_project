n = int(input())
i = 1
count = 1
prevNumber = n

while n != 0:
    n = int(input())
    if n == prevNumber:
        i += 1
    elif n == 0:
        continue
    else:
        if i > count:
            count = i
        i = 1
    prevNumber = n
print(count)
