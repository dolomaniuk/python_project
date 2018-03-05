H = int(input())    # length of pole
A = int(input())    # m up per day
B = int(input())    # m down per night
days = 0
way = 0
while way < H:
    days += 1
    way += A
    if way < H:
        way -= B

print(days)
