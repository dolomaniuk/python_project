a = int(input())
b = int(input())

if a < b:
    for a in range(a, b + 1):
        print(a, end=' ')
else:
    for a in range(a, b - 1, -1):
        print(a, end=' ')
