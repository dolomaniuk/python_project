n = int(input())


def IsPrime(n):
    count = 0
    for i in range(2, n):
        if i > n ** 0.5:
            break
        if n % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


if IsPrime(n):
    print('YES')
else:
    print('NO')
