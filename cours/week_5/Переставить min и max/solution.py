A = list(map(int, input().split()))


def perestan(myList):
    if len(myList) > 1:
        minimum = myList.index(min(myList))
        maximum = myList.index(max(myList))
        if minimum < maximum:
            newList = myList[:minimum]
            newList.append(myList[maximum])
            newList.extend(myList[minimum + 1:maximum])
            newList.append(myList[minimum])
            newList.extend(myList[maximum + 1:])
        else:
            newList = myList[:maximum]
            newList.append(myList[minimum])
            newList.extend(myList[maximum + 1:minimum])
            newList.append(myList[maximum])
            newList.extend(myList[minimum + 1:])
        print(' '.join(map(str, newList)))
    else:
        print(myList[0])


perestan(A)
