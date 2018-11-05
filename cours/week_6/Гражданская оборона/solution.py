n = int(input())
np = list(map(int, input().split()))
# Здесь создали 3-е поле для номера бомбоубежища
for i in range(n):
    np[i] = [np[i], i + 1, 0]
np.sort()

m = int(input())
bu = list(map(int, input().split()))
for i in range(m):
    bu[i] = [bu[i], i + 1]
bu.sort()

# Переменная для начала вложенного цикла
start = 0
for i in range(n):
    # Точка нахождения нужного бомбоубежища
    idx = 0
    # Чтобы минимум был точно больше любого найденного
    minimum = 10e10
    for j in range(start, m):
        tmp = abs(np[i][0] - bu[j][0])
        # Либо обновляем минимум и номер бомбоубежища
        if tmp < minimum:
            idx = j
            minimum = tmp
            np[i][2] = bu[j][1]
        # Либо заканчиваем цикл
        else:
            break
    # Переопределяем начало вложенного цикла
    start = idx

np.sort(key=lambda idx: idx[1])
# Получаем упорядоченный согласно порядка ввода список населённых пунктов и
# назначенных им бомбоубежищ. В качестве отладки такое:
for i in np:
    print(i[2], end=' ')
