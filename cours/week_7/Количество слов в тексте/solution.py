arr = []
with open('in.txt') as fin:
    for line in fin:
        cc = line.split()
        for words in cc:
            arr.append(words)
print(len(set(arr)))
