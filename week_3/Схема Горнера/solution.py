n = int(input())
x = int(input())

i = 0
a = n
p = 0

for i in range(n):
    print('i', i, 'a', a)
    p += a * (n - i) * (x ** (n - i))
    print('p', p)
