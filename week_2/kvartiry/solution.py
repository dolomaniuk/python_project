x = int(input())
y = int(input())
kv = (y - x) + 1    # узнаем кол-во квартир в подъезде
if x == 1:
    print('YES')
elif ((x - 1) % kv) == 0 and (y % kv) == 0:
    print('YES')
else:
    print('NO')
