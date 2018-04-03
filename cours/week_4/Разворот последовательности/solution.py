def pos():
    n = int(input())
    if n != 0:
        pos()
        print(n)
    else:
        print(n)
        return


pos()
