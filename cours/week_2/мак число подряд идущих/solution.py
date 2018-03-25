n = int(input())
i = 1
count = 1
prevNumber = n

while n != 0:
    n = int(input())
    if n == prevNumber:
        i += 1
        if i > count:
            count = i
    elif n == 0:
        continue
    else:
        i = 1
    prevNumber = n
print(count)
