k = int(input())    # кол-во одновременно возможных
m = int(input())    # время обжарки котлеты с 1 стороны
n = int(input())    # кол-во котлет
time = 0
if ((2 * n) % k) != 0:
    print((2 * n) // k)
    time = (2 * n // k + 1) * m
print(time)
