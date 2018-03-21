string = input()
firstH = string.find('h')
lastH = string.rfind('h')
gap = string[firstH + 1: lastH]
print(string[0:firstH + 1] + gap * 2 + string[lastH:])
