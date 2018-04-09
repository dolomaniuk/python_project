N = int(input())
myList = list(map(int, input().split()))
x = int(input())

if myList.count(x) > 0:
    print(x)
else:
    minDelta = abs(x - myList[0])
    for i in range(1, N):
        if abs(x - myList[i]) < minDelta:
            minDelta = abs(x - myList[i])
            closerNumber = myList[i]
    print(closerNumber)
