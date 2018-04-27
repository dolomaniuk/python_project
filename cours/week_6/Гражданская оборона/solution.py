def minDistance(numberOfListN, valueOfNewListM, index):
    listDist = []
    result = []
    count = 0
    # print('index', index)
    # print(valueOfNewListM[index:])
    for ind in valueOfNewListM[index:]:
        tmp = abs(numberOfListN[0] - ind[0]), ind[1], count
        listDist.append(tmp)
        count += 1
    # print('listDist', listDist)
    result = min(listDist, key=lambda p: p[0])
    # print('result[', numberOfListN[1], '] -->', result[2])

    return numberOfListN[1], result[1] + 1, result[2]


# with open('inpData.txt', 'r', encoding='utf8') as fin:
#     data = fin.readlines()
#     tmpList = []
#     for line in data:
#         tmpList.append(line.strip())

n = int(input())
listN = list(map(int, input().split()))
m = int(input())
listM = list(map(int, input().split()))

# n = int(tmpList[0])
# listN = list(map(int, tmpList[1].split()))
# m = int(tmpList[2])
# listM = list(map(int, tmpList[3].split()))

output = []
output = [0] * n
newListN = []
for i in range(n):
    newListN.append([listN[i], i])
newListN.sort(key=lambda pos: pos[0])

newListM = []
for i in range(m):
    newListM.append([listM[i], i])
newListM.sort(key=lambda pos: pos[0])

i = 0
for each in newListN:
    # print('each', each)
    index, value, i = minDistance(each, newListM, i)
    output[index] = value
    if i > 2:
        i -= 1
    # print('i=', i)
for i in output:
    print(i, end=' ')
