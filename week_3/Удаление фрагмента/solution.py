string = input()

first = string.find('h')
revers = string[-1: -len(string) - 1: -1]
last = len(string) - revers.find('h') - 1
# print(first, revers, last)

string = string[0: first] + string[last + 1:]
print(string)
