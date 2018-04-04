flag = ('+___ ', '|{} / ', '|__\ ', '|    ')

n = int(input())

for f in range(0, len(flag)):
    if f == 1:
        for n in range(1, n + 1):
            print(flag[f].format(n), end='')
        print('')
    else:
        print(flag[f] * n)
