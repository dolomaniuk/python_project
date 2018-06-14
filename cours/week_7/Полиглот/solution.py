def inputRightNumberN(countN):
    if countN <= 1 and countN >= 1000:
        print('Error')
        return True
    return False


def inputRightNumberM(countM):
    if countM <= 1 and countM >= 500:
        print('Error')
        return True
    return False


def solve():
    if inputRightNumberN(N) is True:
        return

    else:
        for i in range(N):
            # count of each shoolboy's languages
            countLanguages = int(input())
            if inputRightNumberM(countLanguages) is True:
                return
            # list of each shoolboy's languages
            M = []
            for j in range(countLanguages):
                M.append(input())
            set(M)
            pupils.append(M)

    print(*pupils)


# count of pupils (школьники)
N = int(input())
# list of pupils
pupils = []


solve()