N = int(input())
day = N // (24 * 60)
if day > 0:
    N = N - day * 24 * 60
hour = N % (60 * 24) // 60  # кол-во часов в веденном значении минут
minut = N - (N % (60 * 24) // 60 * 60)           # кол-во оставшихся минут

if minut > 59:
    minut = 0
if hour > 23:
    hour = 0
print(hour, minut)
