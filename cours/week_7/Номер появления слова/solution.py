listWords = []
countWords = []
setWords = set()
with open('input.txt') as fileIn:
    text = fileIn.readlines()
    for string in text:
        listWords += [word for word in string.split()]

countWords += [0 for i in listWords]
print(len(listWords), listWords, sep='\n')
for i in range(len(listWords)):
    if listWords[i] not in setWords:
        setWords.add(listWords[i])
    else:
        countWords[i] += 1
        # countWords.append('0')
print(countWords)
next(i)