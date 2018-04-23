myList = list(map(int, input().split()))
newList = []
for i in range(len(myList)):
    newList.append((myList[i], i))
newList.sort()
print(newList)
