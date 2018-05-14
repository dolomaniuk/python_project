a = {1, 2, 3, 4}
b = {2, 3, 5}
print(a | b)    # объединение
print(a & b)    # пересечение
print(a - b)    # уникальные эл-ты первого
print(a ^ b)    # уникальные элементы

capitals = {'RUSSIA': 'Moscow', 'BELARUS': 'Minsk'}
capitals['USA'] = 'Washington'
# del capitals['USA']
# for count, sity in capitals.items():
#     print(count, sity)

'''
gasCost = {}
n = int(input())
cost = list(map(int, input().split()))
btypes = (92, 95, 98)
for now in range(len(btypes)):
    gasCost[btypes[now]] = cost[now]
for i in range(n - 1):
    cost = list(map(int, input().split()))
    for now in range(len(btypes)):
        gasCost[btypes[now]] = min(cost[now], gasCost[btypes[now]])
print(gasCost[92], gasCost[95], gasCost[98])
'''

s = input()
print(s.isalpha())  # только ли буквы?
print(s.isalnum())  # только ли буквы и цифры?
print(s.isdigit())  # только ли цифры
print(s.lower())  # маленькие
print(s.upper())  # большие
print(s.strip())   # обрезать пробелы по краям
print(s.lstrip())  # обрезать пробелы слева
print(s.rstrip())  # обрезать пробелы справа