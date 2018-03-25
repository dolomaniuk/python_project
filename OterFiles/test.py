def max2(a, b):
    if a > b:
        return a
    return b

def max4(a, b, c, d):
    return max2(max2(a, b), max2(c, d))

print(max2(max2(2, 7), max2(1, 9)))
print(max4(1, 3, 7, 2))