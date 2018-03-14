n = float(input())
n = n * 100
rub = int(n // 100)
coin = round(n % 1000)

print(rub, '{0:02d}'.format(coin % 100))
