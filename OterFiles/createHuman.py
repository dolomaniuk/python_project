from mimesis import Person
import string
import random
import datetime

# Создаем экземпляр класса-провайдера с данными для исландского языка.
# print('Who do you want to create:', '1: ru', '2: eng', sep='\n')
# nation = int(input())
# while not(0 < nation < 3):
#     print('Input only 1 or 2 number')
#     nation = int(input())
nation = 1


def generate_number_passport():
    passport = ''.join(str(random.choice('КЕНВАСМ')) for _ in range(2))
    passport += ''.join(str(random.randint(0, 9)) for _ in range(7))
    return passport


def centuryFromYear(year):
    # вычисление века
    if year % 100 == 0:
        centry = year // 100
    else:
        centry = year // 100 + 1
    return centry


def check_number(pn):
    sum = 0
    for r in pn[0::3]:
        if 47 < ord(r) < 58:
            k = int(r) * 7
            sum += int(r) * 7
        else:
            k = (ord(r) - 55) * 7
            sum += (ord(r) - 55) * 7

    for r in pn[1::3]:
        if 47 < ord(r) < 58:
            k = int(r) * 3
            sum += int(r) * 3
        else:
            k = (ord(r) - 55) * 3
            sum += (ord(r) - 55) * 3

    for r in pn[2::3]:
        if 47 < ord(r) < 58:
            k = int(r)
            sum += int(r)
        else:
            k = (ord(r) - 55)
            sum += (ord(r) - 55)
    sum = sum % 10
    return sum


def generate_id_passport():
    id_passport = []
    now = datetime.datetime.now()
    d_birth = random.randrange(1, 29)
    m_birth = random.randrange(1, 13)
    y_birth = random.randrange(1960, now.year)
    # man = 0, woman = 1
    sex = random.randrange(0, 2)
    century = centuryFromYear(y_birth)

    # определение первой цифры
    if sex == 0:
        if century == 19:
            first_number = 1
        elif century == 20:
            first_number = 3
        elif century == 21:
            first_number = 5
    elif sex == 1:
        if century == 19:
            first_number = 2
        elif century == 20:
            first_number = 4
        elif century == 21:
            first_number = 6

    region_sequence = ['A', 'B', 'C', 'H', 'K', 'E', 'M']
    region = random.choice(region_sequence)
    num_person = ''.join(random.choice(string.digits) for _ in range(3))
    nationality = 'PB'

    id_passport += str(first_number)
    if d_birth < 10:
        id_passport += '0'
    id_passport += str(d_birth)
    if m_birth < 10:
        id_passport += '0'
    id_passport += str(m_birth)
    id_passport += str(y_birth)[2:]
    id_passport += region
    id_passport += num_person
    id_passport += nationality
    id_passport += str(check_number(id_passport))
    id_passport = ''.join(id_passport)

    sex = 'муж' if sex == 0 else 'жен'
    info_id = {
        'sex': sex, 'd_birth': id_passport[1:3], 'm_birth': id_passport[3:5], 'y_birth': str(y_birth),
        'idn': id_passport
    }
    return info_id

def create_human(n):    # function of creating new client
    if n == 1:
        person = Person('ru')
    else:
        person = Person('en')

    # Выводим исландские мужские имена.
    client_info = generate_id_passport()

    print('\nфамилия:\t', person.last_name())
    print('имя:\t\t', person.name())
    print('отчество:\t', person.surname(), '\n')

    passport = generate_number_passport()
    print('личный №:\t', client_info.get('idn'))
    print('документ:\t', passport)

    print('пол:\t\t', client_info.get('sex'))
    print('возраст:\t', person.age(13, 70), '\n')
    # print('аватар\t', person.avatar())
    print('гражд-во:\t', person.get_current_locale())
    print('Нац-сть:\t',person.nationality())
    print('телефон:\t', person.telephone('+37529#######'))
    print('email:\t\t', 'CREDOSPAM@ITWORKS.BY')
    # print('email:\t\t', person.email())
    print('проф-ия:\t', person.occupation(), '\n')
    print('обращение:\t', person.title())
    print('взгляды:\t', person.views_on())
    print('вера:\t\t', person.worldview(), '\n')


create_human(nation)

keys = str(input('Press "Space" and next "Enter" to repeat\nor "Enter" to exit\n'))
try:
    while keys[0] == ' ':
        create_human(nation)
        keys = input('Press "Space" and next "Enter" to create new client again\nor "Enter" to exit\n')
except:
    pass
