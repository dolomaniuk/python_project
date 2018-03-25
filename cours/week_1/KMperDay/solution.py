N = int(input())    # km per day
M = int(input())    # count of day

days = M // N
if M % N > 0:
    days += 1

print(days)
