# with open('inpData.txt', 'r', encoding='utf8') as fin:
#     data = fin.readlines()
#     tmpList = []
#     for line in data:
#         tmpList.append(line.strip())

# print(tmpList)
# print(n, distN)
# print(m, distM)
# print()

# number of shelter
# n = int(tmpList[0])
n = int(input())

# distance each of shelter in n
# distN = list(map(int, tmpList[1].split()))
distN = list(map(int, input().split()))
newListOfDistN = []
for i in range(n):
    newListOfDistN.append((distN[i], i))

# number of bombshelter
# m = int(tmpList[2])
m = int(input())

# distance each of bombshelter in m
# distM = list(map(int, tmpList[3].split()))
distM = list(map(int, input().split()))
newListOfDistM = []
for i in range(m):
    newListOfDistM.append((distM[i], i))

newMinList = []
tmp = []
for i in range(n):
    for j in range(m):
        tmp = abs(newListOfDistM[j][0] - newListOfDistN[i][0]), j + 1
        newMinList.append(list(tmp))
    print(min(newMinList, key=lambda newMinList: newMinList[0])[1], end=' ')
    newMinList = []
