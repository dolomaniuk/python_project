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
    if inputRightNumberN(N):
        return
    else:
        for i in range(N):
            # count of each shoolboy's languages
            countLanguages = int(input())
            if inputRightNumberM(countLanguages):
                return
            # list of each shoolboy's languages
            M = set()
            for j in range(countLanguages):
                lang = input()
                M.add(lang)
                diffLanguages.add(lang)
            pupils.append(M)

    # языки, которые знает каждый ученик
    for each in pupils:
        commonLanguages = each & pupils[0]
    print(len(commonLanguages), *commonLanguages, sep='\n')

    # the all difference languages
    print(len(diffLanguages), *diffLanguages, sep='\n')


# count of pupils (школьники)
N = int(input())
# list of pupils
pupils = []
# set of all difference languages
diffLanguages = set()
# set of all common languages
commonLanguages = set()
solve()
