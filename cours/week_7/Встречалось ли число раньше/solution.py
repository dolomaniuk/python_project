N = list(map(int, input().split()))
setN = set(N)
for i in N:
    if i in setN:
        print('NO')
        setN.remove(i)
    else:
        print('YES')
