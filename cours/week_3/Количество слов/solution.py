string = input()

countWord = string.count(' ')
if countWord == 0:
    print(1)
elif countWord > 0:
    print(countWord + 1)
