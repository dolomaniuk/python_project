string = input()
posBack = string.find(' ')
a = string[0:posBack]
b = string[posBack + 1:]
a, b = b, a
string = a + ' ' + b
print(string)
