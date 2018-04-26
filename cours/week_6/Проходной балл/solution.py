PassExam = True
scoreList = []      # [0] кол-во проходных учеников

with open('input.txt', 'r', encoding='utf8') as fileIn:
    k = int(fileIn.readline())
    scoreList.append(0)
    for line in fileIn.readlines():
        data = line.split()
        egeScores = list(map(int, data[-3:]))
        for i in egeScores:
            if i < 40:
                PassExam = False
        if PassExam:
            score = sum(egeScores)
            scoreList[0] += 1
            scoreList.append(score)
        PassExam = True

scoreList.sort(reverse=True)
# print(scoreList)

if scoreList[-1] <= k and scoreList[-1] != 0:
    print(0)
else:
    if scoreList.count(scoreList[0]) > k:
        print(1)
    else:
        newList = []
        for i in range(k + 1):
            newList.append(scoreList[i])
        newList.sort()
        # print(newList)

        equal = 1
        for i in range(k):
            if newList[i] == newList[i + 1]:
                equal += 1
            else:
                break
        if equal == 1:
            print(min(newList))
        else:
            print(scoreList[k - equal])
