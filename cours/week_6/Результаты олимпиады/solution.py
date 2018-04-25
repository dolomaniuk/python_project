N = int(input())

mylist = []
for i in range(N):
    string = input().split()
    temp = string[0], string[1]
    mylist.append(list(temp))
mylist.sort(key=lambda p: int(p[1]), reverse=True)
for lastName in mylist:
    print(lastName[0])
