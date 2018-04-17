listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
listC = []
lenListC = len(listA) + len(listB)


def merge(A, B):
    for i in range(lenListC):
        if (len(A) > 0) and (len(B) > 0):
            if A[0] < B[0]:
                listC.append(A.pop(0))
            else:
                listC.append(B.pop(0))
        elif len(A) > 0:
            listC.append(A.pop(0))
        elif len(B) > 0:
            listC.append(B.pop(0))

    return listC


print(*merge(listA, listB))
