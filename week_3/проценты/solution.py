P = int(input())
X = int(input())
Y = int(input())

S = X * 100 + Y
S = int(S * (100 + P) / 100)

print(S // 100, S % 100)
