string = input()

num = 0
pos = string.find('f')
# print(pos)
if pos == -1:
    num = -2
else:
    if string.find('f', pos + 1) == -1:
        num = -1
    else:
        num = string.find('f', pos + 1)
print(num)
