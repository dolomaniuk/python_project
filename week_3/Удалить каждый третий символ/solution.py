string = input()
i = 0
newStr = ''
while i < len(string):
    if i == 0 or (i % 3 == 0):
        i += 1
    else:
        newStr += string[i]
        i += 1
print(newStr)
