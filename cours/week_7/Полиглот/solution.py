def inputRightNumberN(countN):
    if countN < 1 or countN > 1000:
        print('Error')
        return True
    return False


def inputRightNumberM(countM):
    if countM < 1 or countM > 500:
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
            pupils.append(set(M))

    # языки, которые знает каждый ученик
    commonLanguages = []
    for each in pupils:
        commonLanguages = each & pupils[0]
    print(len(commonLanguages), *commonLanguages, sep='\n')

    # max count languages that knows boy
    differentLanguages = set()
    for each in pupils:
        differentLanguages |= each
    print(len(differentLanguages), *differentLanguages, sep='\n')
    # print(len(max(pupils)), *pupils[pupils.index(max(pupils))], sep='\n')


# count of pupils (школьники)
N = int(input())
# list of pupils
pupils = []


solve()
