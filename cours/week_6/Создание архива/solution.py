S = list(map(int, input().split()))
arr_spaces = []
summa = 0

for i in range(S[1]):
    arr_spaces.append(int(input()))
arr_spaces.sort()

while sum(arr_spaces) > S[0]:
    arr_spaces.pop()

print(len(arr_spaces))
