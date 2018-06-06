import sys

arr = []

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    cc = line.split()
    for words in cc:
        arr.append(words)
    else:
        break
print(len(set(arr)))
