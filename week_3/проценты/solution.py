from math import ceil
P = int(input())
X = int(input())
Y = int(input())

d = 1
S = X * 100 + Y

while d <= 365:
    percentDay = round(S * P / 100 / 365)
    S += percentDay
    # print(S / 100, S % 100)
    d += 1

print(S / 100)
