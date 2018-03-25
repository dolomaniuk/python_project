n = int(input())
a = n // 100
a1 = n // 10 % 10
a2 = n % 10
print(a, a1, a2, sep=' + ', end=' ')
print('=', a+a1+a2)
