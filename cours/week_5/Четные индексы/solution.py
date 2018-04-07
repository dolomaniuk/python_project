myList = list(map(int, input().split()))
newList = ''
for i in range(len(myList)):
    if i % 2 == 0:
        print(myList[i], end=' ')
