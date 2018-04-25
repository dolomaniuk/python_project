myList = list(map(int, input().split()))


def CountSort(A):
    newList = [0] * 100
    for num in A:
        newList[num] += 1
    # print(newList)
    for i in range(100):
        # if newList[i] > 0:
        print((str(i) + ' ') * newList[i], end='')


CountSort(myList)
