from heapq import merge
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listC = merge(listA, listB)

print(*listC)
