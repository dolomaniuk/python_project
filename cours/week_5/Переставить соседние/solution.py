myList = list(map(int, input().split()))
newList = []

if len(myList) % 2 == 0:
    for i in range(len(myList)):
        if i % 2 != 0:
            newList.append(myList[i])
            newList.append(tmp)
        else:
            tmp = myList[i]
else:
    for i in range(0, len(myList) - 1):
        if i % 2 != 0:
            newList.append(myList[i])
            newList.append(tmp)
        else:
            tmp = myList[i]
    newList.append(myList[len(myList) - 1])
print(' '.join(map(str, newList)))
