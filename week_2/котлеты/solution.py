k = int(input())    # кол-во одновременно возможных
m = int(input())    # время обжарки котлеты с 1 стороны
n = int(input())    # кол-во котлет
time = 0
if n > k:
    while n > 0:
        time += k * (2 * m)
        n -= k
elif n <= k:
    time = k * (2 * m)

print(time)
