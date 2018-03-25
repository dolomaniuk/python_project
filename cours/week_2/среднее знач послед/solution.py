n = int(input())
i = 1
count = n

while n != 0:
    n = int(input())
    if n == 0:
        continue
    i += 1
    count += n

print(count / i)
