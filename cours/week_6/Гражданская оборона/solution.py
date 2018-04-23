from collections import namedtuple

arrShel = []
arrBombShel = []
result = []

# number of shelter
n = int(input())
# distance each of shelter in n
distN = list(map(int, input().split()))
newListOfDistN = []
for i in range(len(distN)):
    newListOfDistN.append((distN[i], i))
newListOfDistN.sort()
# number of bombshelter
m = int(input())
# distance each of bombshelter in m
distM = list(map(int, input().split()))
newListOfDistM = []
for i in range(len(distM)):
    newListOfDistM.append((distM[i], i))
newListOfDistM.sort()

newMinList = []
print(newListOfDistM[0][0], '----')
tmpMin = newListOfDistM[0][1]

for i in range(len(newListOfDistN)):
    for j in range(len(newListOfDistM)):
        tmp = abs(newListOfDistM[j][0] - newListOfDistN[i][0])
        print(abs(newListOfDistM[j][0] - newListOfDistN[i][0]))
        if tmp < tmpMin:
            tmpMin = tmp
            print('!!', newListOfDistM[j][1])
            newMinList.append(newListOfDistM[j][1])

print(newMinList)
