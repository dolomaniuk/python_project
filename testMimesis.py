from mimesis import Person

# Создаем экземпляр класса-провайдера с данными для исландского языка.
print('Input number of language:', '1: ru', '2: eng', sep='\n')
nation = int(input())
while not(0 < nation < 3):
    print('Input only 1 or 2 number')
    nation = int(input())


def createHuman(n):
    if n == 1:
        person = Person('ru')
    else:
        person = Person('en')

    # Выводим исландские мужские имена.

    print('\nфамилия:\t', person.last_name())
    print('имя:\t\t', person.name())
    print('отчество:\t', person.surname(), '\n')
    print('пол:\t\t', person.gender())
    print('возраст:\t', person.age(13, 70), '\n')
    # print('аватар\t', person.avatar())
    print('гражд-во:\t', person.get_current_locale())
    print('Нац-сть:\t',person.nationality())
    print('телефон:\t', person.telephone('+37529#######'))
    print('email:\t\t', person.email())
    print('проф-ия:\t', person.occupation(), '\n')
    print('обращение:\t', person.title())
    print('взгляды:\t', person.views_on())
    print('вера:\t\t', person.worldview(), '\n')


createHuman(nation)
