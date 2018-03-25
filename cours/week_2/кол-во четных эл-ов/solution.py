n = -1
count = 0

while n != 0:
    n = int(input())
    if n == 0:
        continue
    if n % 2 == 0:
        count += 1

print(count)
