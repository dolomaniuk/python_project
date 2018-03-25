string = input()

first = string.find('h')
last = string.rfind('h')
gap = string[first + 1: last].replace('h', 'H')
print(string[0:first + 1] + gap + string[last:])
