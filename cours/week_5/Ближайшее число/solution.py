N = int(input())
myList = list(map(int, input().split()))
x = int(input())
newList = []

if myList.count(x) > 0:
    print(x)
else:
    if x > 0:
        for i in range(N):
            newList.append(abs(x - myList[i]))
            # print('1', abs(x - myList[i]))
    else:
        for i in range(N):
            newList.append(x - myList[i])
            # print('2', x - myList[i])
    # print(newList)
    ind = newList.index(min(newList))
    print(myList[ind])
