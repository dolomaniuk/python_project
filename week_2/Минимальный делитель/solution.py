'''
Дано целое число, не меньшее 2. Выведите его
 наименьший натуральный делитель, отличный от 1
'''
N = int(input())
i = 2   # variable

while i <= N:
    if (N % i) == 0:
        print(i)
        i = N
    i += 1
