myList = list(map(int, input().split()))
i = 0

while i < len(myList):  # del negative numbers
    if myList[i] < 1:
        myList.pop(i)
        continue
    i += 1
# print(myList)
minimum = myList[0]
i = 0
while i < len(myList):
    # print(i, myList[i], minimum)
    if myList[i] < minimum:
        minimum = myList[i]
    i += 1
print(minimum)
