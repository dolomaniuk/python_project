listWords = {}  # словарь в виде номер слова: (слово: кол-во раз встречается)
tmp = {}
count = 1
result = []
with open('input.txt') as fileIn:
    text = fileIn.readlines()
    for string in text:
        for word in string.split():
            listWords[count] = {word: 0}
            count += 1
for count in listWords.keys():
    key = list(listWords[count].items())
    # (key[0][0]) - сам ключ в словаре под номером count
    if key[0][0] in tmp:
        tmp[key[0][0]] += 1  # увеличиваем счетчик появление слова
        listWords[count][key[0][0]] = tmp[key[0][0]]
    else:
        tmp[key[0][0]] = 0    # добавляем новое слово в словарь
    result.append(tmp[key[0][0]])
# print(*listWords.values(), sep='\n')
print(*result)
