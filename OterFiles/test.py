from collections import namedtuple

p = []
n = int(input())
for i in range(n):
    man = namedtuple('man', 'height name')
    man.height, man.name = input().split()
    p.append(man)


def makeTuple(man):
    return (man.height, man.name)


p.sort(key=makeTuple)
for now in p:
    print(now.height, now.name)
