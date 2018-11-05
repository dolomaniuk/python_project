# вводим лимит чисел
n = int(input())
# образуем множество доступных ответов
valid_answer = set(range(1, n + 1))

beatreace_message = ''  #ответ Биатрис
while beatreace_message.upper() != 'HELP':  #пока Биатрис не просит хелп
    beatreace_message = input()     #ответ Биатрис
    try:
        #преобразуем ответ из чисел в множество
        attempt_request = set(map(int, beatreace_message.split()))
        #ответ Августа, есть ли в ответе Биатрис загаданное число
        answer = str(input())
        if answer.upper() == 'NO':
            #вычитаем из возможных ответов, числа Биатрис
            #оставляем уникальные значения в множестве возм. ответов
            valid_answer -= attempt_request
        elif answer.upper() == 'YES':
            #обрезаем множество возм.значений до значений чисел Биатрис
            #пересечение множеств
            valid_answer &= attempt_request
            #если точно назвала цифру
            if len(attempt_request) == 1:
                print(beatreace_message)
                break
    except ValueError:      #ответ Биатрис был не числом, а просьбой хелп
        print(*sorted(valid_answer))
