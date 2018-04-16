listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
listC = []
i = 0
lenListC = len(listA) + len(listB)
def merge(A, B):
    while len(listC) < lenListC:
        if (A[0] is None) and (B[0] is not None):
            print('0')
            if A[0] < B[0]:
                listC.append(A[0])
                A.remove(A[0])
            else:
                listC.append(B[0])
                B.remove(B[0])
        elif A[0] is None:
            print('1')
            listC.append(B[0])
        elif B[0] is None:
            print('2')
            listC.append(A[0])

    return listC

print(merge(listA, listB))