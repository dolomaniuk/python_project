with open('inpData.txt', 'r', encoding='utf8') as fin:
    data = fin.readlines()
    tmpList = []
    for line in data:
        tmpList.append(line.strip())

# n = int(input())
# distN = list(map(int, input().split()))
# m = int(input())
# distM = list(map(int, input().split()))

n = int(tmpList[0])
distN = list(map(int, tmpList[1].split()))
m = int(tmpList[2])
distM = list(map(int, tmpList[3].split()))

# print(tmpList)
# print(n, distN)
# print(m, distM)
# print()

# number of shelter



# distance each of shelter in n
# number of bombshelter
# distance each of bombshelter in m

newListOfDistM = []
for i in range(m):
    newListOfDistM.append((distM[i], i))
sortDistM = sorted(newListOfDistM, key=lambda newListOfDistM:newListOfDistM[0])

newMinList = []
tmp = []

x = []

for i in range(n):
    tmp1 = abs(sortDistM[0][0] - distN[i]), 1
    for j in range(m):
        tmp = abs(sortDistM[j][0] - distN[i]), j + 1
        if tmp > tmp1:
            print('dist1', newListOfDistM[j - 1][0])
            tmp = tmp1
        elif tmp == tmp1:
            print('dist2', newListOfDistM[j - 1][0])
            # newMinList.append(list(tmp))
        else:
            continue
    newMinList.append(list(tmp))
    x = min(newMinList, key=lambda newMinList: newMinList[0])[1]
    print(x)
    newMinList = []
