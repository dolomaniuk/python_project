from collections import namedtuple

arrShel = []
arrBombShel = []
result = []

# number of shelter
n = int(input())
# distance each of shelter in n
distN = list(map(int, input().split()))
for i in range(n):
    shelter = namedtuple('Shelter', 'distance number')
    shelter.distance = distN[i]
    shelter.number = i
    arrShel.append(shelter)
# number of bombshelter
m = int(input())
# distance each of bombshelter in m
distM = list(map(int, input().split()))
for i in range(m):
    bombshelter = namedtuple('Bombshelter', 'distance number')
    bombshelter.distance = distM[i]
    bombshelter.number = i
    arrBombShel.append(bombshelter)

arrShel.sort(key=lambda shelter: (shelter.distance ** 2, shelter.number))
for now in arrShel:
    print(now.distance, now.number)
arrBombShel.sort(key=lambda bombshelter: (bombshelter.distance ** 2, bombshelter.number))
for now in arrBombShel:
    print(now.distance, now.number)

res = []
for i in arrShel:
    for j in arrBombShel:
        res = namedtuple('Result', 'distance number')
        res.distance = abs(int(arrShel[i].distance) - int(arrBombShel[j].distance))
        res.number = arrBombShel[j].number
        result.append(tuple(res.distance, res.number))
        print(*result)
