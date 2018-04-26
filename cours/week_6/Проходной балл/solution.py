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
# print(scoreList[-1])
with open('output.txt', 'w', encoding='utf8') as fout:
    if scoreList.count(scoreList[0]) > k:
        print(1, file=fout)
    elif 0 < scoreList[-1] <= k:
            print(0, file=fout)
    elif scoreList[-1] == 0:
        print('', file=fout)
    elif scoreList.count(scoreList[0]) == k:
        print('', file=fout)
    else:
        passScore = scoreList[k]
        if scoreList[k - 1] == scoreList[k]:
            for scr in scoreList[k - 2::-1]:
                if scr != passScore:
                    passScore = scr
                    break
                else:
                    continue
        print(passScore, file=fout)
