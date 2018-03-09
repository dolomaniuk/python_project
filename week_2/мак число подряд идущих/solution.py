n = int(input())
count = 1
prevNumber = n

while n != 0:
    n = int(input())
    if n == prevNumber:
        count += 1
    elif n == 0:
        continue
    else:
        count = 1
    prevNumber = n
print(count)
