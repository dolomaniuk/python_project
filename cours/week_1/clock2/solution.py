iSec = int(input())     # сколько прошло секунд всего
day = iSec // (24*3600)
iSec = iSec - day * 24 * 3600
hour = iSec // 3600     # сколько прошло часов с начала
if hour > 0:
    min = iSec % (hour * 3600) // 60        # сколько прошло минут с начала
else:
    min = iSec // 60
sec = iSec - (hour * 3600) - (min * 60)   # сколько прошло секунд с начала
if hour > 23:
    hour = 0
if (min // 60) >= 1:    # преобразуем минуты в часы
    min = 0
if min < 10:            # добавляем "0" к минутам, если число меньше 10
    min = '0' + str(min)
if sec < 10:            # добавляем "0" к секундам, если число меньше 10
    sec = '0' + str(sec)
print(hour, min, sec, sep=':')
