string = input()
i = 0
newStr = ''
if len(string) > 1:
    while i < len(string):
        if i == (len(string) - 1):
            newStr += string[i]
            i += 1
            continue
        else:
            newStr += string[i] + '*'
        i += 1
else:
    newStr = string
print(newStr)
