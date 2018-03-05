n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 <= n2:
    if n2 <= n3 or n1 <= n3:
        print(n3)
    else:
        print(n2)
else:
    if n1 <= n3:
        print(n3)
    else:
        print(n1)
