with open('input.txt') as inf:
    count = {}
    for line in inf:
        words = list(line.strip().split())
        for word in words:
            count[word] = count.get(word, 0) + 1
            print(int(count[word] - 1), end=" ")
