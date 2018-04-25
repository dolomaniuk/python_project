with open('input.txt', 'r', encoding='utf8') as fin:
    data = fin.readlines()


class Junior:
    lastName = ''
    name = ''
    scoring = 0


temList = []
for line in data:
    jun = Junior()

    line = line.split()
    jun.lastName = line[0]
    jun.name = line[1]
    jun.scoring = line[3]
    temList.append(jun)

temList.sort(key=lambda p: p.lastName)

with open('output.txt', 'w', encoding='utf8') as fout:
    for man in temList:
        print(man.lastName, man.name, man.scoring, file=fout)
