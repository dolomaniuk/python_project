sting = input()

length = len(sting)

print(sting[2])     # второй
print(sting[length - 2])    # предпоследний
print(sting[0:5])   # первые 5
print(sting[0:length - 2])  # вся строка, кроме 2 последних
print(sting[::2])  # четные
print(sting[1::2])  # нечетные
print(sting[-1:-length-1:-1])  # в обратном порядке
print(sting[-1:-length-1:-2])  # в обратном порядке
print(length)  # в обратном порядке
