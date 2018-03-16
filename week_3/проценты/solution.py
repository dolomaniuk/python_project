from math import floor
P = int(input())
X = int(input())
Y = int(input())

S = X * 100 + Y

S *= 1 + P / 100
# print(S % 100)
print(int(S / 100), floor(S % 100))
