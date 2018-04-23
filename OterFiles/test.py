with open('inpData.txt', 'r', encoding='utf8') as fin:
    data = fin.readlines()
    tmpList = []
    for i in data:
        tmpList.append(i.strip())
print(tmpList)
n = int(tmpList[0])
distN = list(map(int, tmpList[1].split()))
m = int(tmpList[2])
distM = list(map(int, tmpList[3].split()))

print(n, distN)
print(m, distM)
