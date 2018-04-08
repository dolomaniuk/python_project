myList = list(map(int, input().split()))
newList = []
for i in range(len(myList)):
    if myList[i] > 0:
        newList.append(myList[i])
print(len(newList))
