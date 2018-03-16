P = int(input())
X = int(input())
Y = int(input())

S = X + Y / 100
S *= 1 + P / 100
coin = round(100 * (S - (int(S))))
# print(100 * (S - (int(S))))
print(int(S), coin)
