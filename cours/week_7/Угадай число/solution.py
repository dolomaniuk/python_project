from random import randint

n = int(input())
aug_number = randint(1, n)
# print(aug_number)
answers = []
inp_str = input()
while inp_str.upper() != 'HELP' and not inp_str.isalpha():
    b_answer = list(map(int, inp_str.split()))
    for num in b_answer:
        answers.append(num)
    if aug_number in b_answer:
        print('YES')
        if b_answer[0] == aug_number and len(b_answer) == 1:
            for i in answers:
                if i == b_answer[0]:
                    answers.remove(i)
            break
    else:
        print('NO')
    inp_str = input()

result = set(range(1, n + 1)) - set(answers)
print(*sorted(result))
