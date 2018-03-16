P = int(input())
X = int(input())
Y = int(input())
K = int(input())

S = X * 100 + Y
year = 1
while year < (K + 1):
    S = int(S * (100 + P) / 100)
    year += 1
print(S // 100, S % 100)
