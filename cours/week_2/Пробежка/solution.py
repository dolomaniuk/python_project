"""
Пробежка
"""
x = float(input())
y = float(input())

day = 1
way = x

while way < y:
    day += 1
    way = way + ((way * 10) / 100)
print(day)
