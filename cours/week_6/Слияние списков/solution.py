listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
listC = []
lenListC = len(listA) + len(listB)

lenghtA = len(listA)
lenghtB = len(listB)


def merge(A, B):
    Ai = 0  # counter
    Bi = 0  # counter
    while len(listC) < lenListC:
        if (Ai < lenghtA) and (Bi < lenghtB):
            if A[Ai] < B[Bi]:
                listC.append(A[Ai])
                Ai += 1
            else:
                listC.append(B[Bi])
                Bi += 1
        elif Ai <= lenghtA:
            listC.append(A[Ai])
            Ai += 1
        elif Bi <= lenghtB:
            listC.append(B[Bi])
            Bi += 1

    return listC


print(*merge(listA, listB))
