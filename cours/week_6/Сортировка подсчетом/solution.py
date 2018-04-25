myList = list(map(int, input().split()))


def CountSort(A):
    newList = [0] * len(A)
    for num in A:
        print(num)
        for i in range(num):
            newList[i] += 1
        print(newList)


CountSort(myList)
