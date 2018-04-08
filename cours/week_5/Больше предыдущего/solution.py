mylist = list(map(int, input().split()))
maxim = mylist[0]
newList = []

for i in range(0, len(mylist)):
    if mylist[i] > maxim:
        maxim = mylist[i]
        newList.append(mylist[i])
    else:
        maxim = mylist[i]
print(' '.join(map(str, newList)))
