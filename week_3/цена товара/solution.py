import math
n = float(input())
n = n * 100
rub = int(n // 100)
coinD = math.floor(((n % 100) - (n % 10)) / 10)
coinS = int(n % 10)

print(rub, str(coinD) + str(coinS))
