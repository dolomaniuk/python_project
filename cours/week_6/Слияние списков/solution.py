A = list(map(int, input().split()))
B = list(map(int, input().split()))
newlist = []


def merge(list1, list2):
    while list1 and list2:
        if list1[0] == list2[0]:
            newlist.append(list1.pop(0))
            newlist.append(list2.pop(0))
        elif list1[0] < list2[0]:
            newlist.append(list1.pop(0))
        else:
            newlist.append(list2.pop(0))

    if list1:
        newlist.extend(list1)
    if list2:
        newlist.extend(list2)

    return newlist


print(*merge(A, B))
