import random
n = int(input())
if (n // 10**3) > 0:    # значит число 4х значное
    first = n // 1000
    second = (n // 100) % 10
    third = (n // 10) % 10
    fourht = n % 10
else:               # если 3х значное число - добавляем "0" в перед числа
    first = 0
    second = (n // 100) % 10
    third = (n // 10) % 10
    fourht = n % 10

if (first == fourht) & (second == third):
    print(1)
else:
    print(int(random.uniform(0, 100)))
