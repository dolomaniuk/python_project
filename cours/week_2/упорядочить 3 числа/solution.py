a = int(input())
b = int(input())
c = int(input())

while (a > b) or (b > c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

print(a, b, c)
