myList = list(map(int, input().split()))
maximum = myList[0]
for i in range(0, len(myList)):
    # print('i:', i, 'max:', maximum, 'myList[i]:', myList[i])
    if myList[i] >= maximum:
        maximum = myList[i]
        indx = i
indx = myList.index(maximum, indx)
print(maximum, indx)
