N = int(input())
myList = list(map(int, input().split()))
x = int(input())

# if myList.count(x) > 0:
#     print(x)
# else:
minDelta = abs(abs(x) - myList[0])
for i in range(1, N):
    delta = abs(abs(x) - myList[i])
    if delta < minDelta:
        minDelta = delta
        closerNumber = myList[i]
print(closerNumber)
