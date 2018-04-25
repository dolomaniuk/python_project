myList = list(map(int, input().split()))

newList = [0] * 101


def CountSort(A):
    for num in A:
        newList[num] += 1
    # print(newList)
    for i in range(101):
        # if newList[i] > 0:
        print((str(i) + ' ') * newList[i], end='')


CountSort(myList)
