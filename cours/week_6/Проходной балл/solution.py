class Students:
    FIO = ''
    score = 0
    passExam = True

listOfStudentes = []
passScore = 0
countPass = 0
countFail = 0
passStudentesList = []
scoringEqualing = True

with open('input.txt', 'r', encoding='utf8') as fileIn:
    k = int(fileIn.readline())

    for line in fileIn.readlines():
        student = Students()
        data = line.split()
        student.FIO = ' '.join(data[0:-3])
        egeScores = list(map(int, data[-3:]))
        student.score = sum(egeScores)
        for i in egeScores:
            if i < 40:
                student.passExam = False

        if not student.passExam:
            countFail += 1
        else:
            countPass += 1
            passStudentesList.append(student)

        listOfStudentes.append(student)

listOfStudentes.sort(key=lambda p: p.score, reverse=True)
passScore = listOfStudentes[k - 1].score
# print('k=', k, 'passScore=', passScore)
# print('countFail', countFail, 'countPass', countPass)

if countPass <= k:
    print(0)
elif countPass > k:
    scoring = passStudentesList[0].score
    for std in passStudentesList:
        if std.score != scoring:
            scoringEqualing = False
    if scoringEqualing:
        print(1)
    else:
        print(passScore)
else:
    print(passScore)
