string = input()

first = 0
pos = string.find('f')
if pos != -1:
    first = pos
    pos = string.find('f', pos + 1)
    if pos != -1:
        string = string[-1: -len(string) - 1: -1]
        pos = len(string) - string.find('f') - 1
        print(first, pos)
    else:
        print(first)
