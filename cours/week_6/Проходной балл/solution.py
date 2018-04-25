Pass = True
listOfScore = []

with open('input.txt', 'r', encoding='utf8') as fileIn:
    k = int(fileIn.readline())

    for line in fileIn.readlines():
        data = line.split()
        egeScores = list(map(int, data[-3:]))
        for i in egeScores:
            if i < 40:
                Pass = False
        if Pass:
            score = sum(egeScores)
            listOfScore.append(score)
        Pass = True

listOfScore.sort(reverse=True)
print(listOfScore)
tmpScore = listOfScore[0]


countMax = listOfScore.count(listOfScore[k - 1])
lastIndexK = listOfScore.index(listOfScore[k - 1], k)
print('countMax=', countMax, 'ind', lastIndexK)

if countMax >= k:
    print(1)
elif 0 < len(listOfScore) < k:
    print(0)
elif len(listOfScore) == 0:
    print("")
else:
    # pass scoring bal
    for scr in range(lastIndexK, -1, -1):
        if listOfScore[scr] == listOfScore[lastIndexK]:
            continue
        else:
            passScore = listOfScore[scr]
            break
    print(passScore)