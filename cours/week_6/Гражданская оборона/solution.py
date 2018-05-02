# n = int(input())
# listN = list(map(int, input().split()))
# m = int(input())
# listM = list(map(int, input().split()))

with open('inpData.txt', 'r', encoding='utf8') as fin:
    data = fin.readlines()
    tmpList = []
    for line in data:
        tmpList.append(line.strip())

n = int(tmpList[0])
listN = tuple(map(int, tmpList[1].split()))
m = int(tmpList[2])
listM = tuple(map(int, tmpList[3].split()))

if m == 1:
    for each in listN:
        print(1)
elif m > 1:
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
    j = 0
    for eachN in newListN:
        # print('____eachN____', eachN)
        # print(newListM)
        distFirst = 100000
        # print('j=', j, 'distF=', distFirst)
        # print('srez', newListM[j:])
        for jM in newListM[j:]:
            # print('jM', jM)
            distSec = abs(eachN[0] - jM[0])
            # print('distSec', distSec)
            if distSec < distFirst:
                output[eachN[1]] = jM[1] + 1
                # print('output[', eachN[1], ']=', output[eachN[1]])
                j = newListM.index(jM)
                # print('index:', j)
                distFirst = distSec
                # print('distSF=', distFirst)
                continue
            else:
                break
    print(*output)
else:
    pass
