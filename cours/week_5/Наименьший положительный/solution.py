myList = list(map(int, input().split()))
i = 0
minimum = 0
print(len(myList))
while i < len(myList):
    print('i:', i, 'mylist:', myList[i])
    if myList[i] < 0:
        myList.pop(i)
    i += 1
print(myList)
