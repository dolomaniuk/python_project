from collections import namedtuple

# arrShel = []
# arrBombShel = []
# result = []

with open('inpData.txt', 'r', encoding='utf8') as fin:
    data = fin.readlines()
    tmpList = []
    for line in data:
        tmpList.append(line.strip())

print(tmpList)
n = int(tmpList[0])
distN = list(map(int, tmpList[1:n + 1]))
m = int(tmpList[n + 1])
distM = list(map(int, tmpList[n + 2:]))

print(n, distN)
print(m, distM)
print()

# number of shelter
# n = int(input())
# distance each of shelter in n
# distN = list(map(int, input().split()))
newListOfDistN = []
for i in range(len(distN)):
    newListOfDistN.append((distN[i], i))
# newListOfDistN.sort()
print(newListOfDistN)
# number of bombshelter
# m = int(input())
# distance each of bombshelter in m
# distM = list(map(int, input().split()))
newListOfDistM = []
for i in range(len(distM)):
    newListOfDistM.append((distM[i], i))
# newListOfDistM.sort()
print(newListOfDistM)
newMinList = []
print('tmpMin', abs(newListOfDistM[0][0] - newListOfDistN[0][0]))
tmpMin = abs(newListOfDistM[0][0] - newListOfDistN[0][0])

for i in range(len(newListOfDistN)):
    for j in range(len(newListOfDistM)):
        tmp = abs(newListOfDistM[j][0] - newListOfDistN[i][0])
        print('dist', tmp, end=' ')
        if tmp <= tmpMin:
            tmpMin = tmp
            index = newListOfDistM[j][1]
            print('index', newListOfDistM[j][1])
    newMinList.append(newListOfDistM[index][1] + 1)
    print('_______')
print(*newMinList)
