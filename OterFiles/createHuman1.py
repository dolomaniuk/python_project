from mimesis import Person
import string
import random
import pyautogui
import xerox    # for ctrl+c/ctrl+v
from transliterate import translit, get_available_language_codes
from datetime import date

pyautogui.PAUSE = 0.1
personalData = {'lastname': 'петров',
                'name': 'вася',
                'surname': 'евгеньевич',
                'gender': 'Муж.',
                'age': ('20','04','1987'),
                'passport': 'AB1111111',
                'mobile': '+375291111111',
                'email': 'CREDOSPAM@ITWORKS.BY'}
age = []    # возраст

def currentDate():
    day = date.today().day
    month = date.today().month
    year = date.today().year
    if day < 10:
        age.append('0' + str(day))
    else:
        age.append(str(day))
    if month < 10:
        age.append('0' + str(month))
    else:
        age.append(str(month))
    age.append(str(year))
    return age

# function of copy data in clipboard with next paste
def copyPaste(value):
    xerox.copy(value)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    print(value)

# function of inserting data in field on web-page
def selfData(dict):
    xerox.copy(dict['lastname'])
    pyautogui.doubleClick(400, 307)     # set cursor on Familiya
    pyautogui.hotkey('ctrl', 'v')

    copyPaste(dict['name'])             # type Name
    copyPaste(dict['surname'])          # type surname

    pyautogui.press('tab')
    if personalData['gender'] == 'Муж.':
        pyautogui.press('left')         # set male
    else:
        pyautogui.press('right')        # set female

    copyPaste(translit(dict['name'], 'ru', reversed=True))      # type latin Name
    copyPaste(translit(dict['lastname'], 'ru', reversed=True))  # type latin LastName

    pyautogui.click(318, 505)           # set cursor on Резиденство
    pyautogui.hotkey('home')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.press('tab')              # set date of birthday
    for i in range(3):
        pyautogui.typewrite(personalData['age'][i])

################################## DUL #####################

    print('Wait pls:', end=' ')
    pyautogui.click(190, 890)           # click on deactivate button

    for i in range(15, 0, -1):
        print(i, end=' ')
        pyautogui._autoPause(1, 1)
    print('')

    pyautogui.click(380, 690)           # click on type of dockument
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.press('tab')

    copyPaste(dict['passport'])         # type passport
    copyPaste('МОСКОВСКИЙ РОВД Г.БРЕСТА')   # type who took

    pyautogui.press('tab')
    pyautogui.typewrite('05032001')     # type date out of document
    pyautogui.press('tab')
    pyautogui.typewrite('06032025')     # type who took

################################## BirthPlace #####################

    pyautogui.press('tab')
    pyautogui.hotkey('home')
    pyautogui.press('down')
    pyautogui.press('enter')

    for i in range(3):
        pyautogui.press('tab')

    copyPaste('БРЕСТ')                  # type City

################################## REGISTRATION #####################

    pyautogui.press('tab')              # country
    # pyautogui.hotkey('home')
    # pyautogui.press('down')
    # pyautogui.press('enter')
    #
    # print('Wait...5 sec')
    # pyautogui._autoPause(5, 1)

    pyautogui.press('tab')
    pyautogui.typewrite('224002')       # type index

    copyPaste('БРЕСТСКАЯ')              # type область
    copyPaste('ЮЖНЫЙ')                  # type район

    pyautogui.press('tab')

    copyPaste('БРЕСТ')                  # type City

    pyautogui.press('tab')

    copyPaste('МОСКОВСКАЯ')             # type street

    pyautogui.press('tab')
    pyautogui.typewrite('13')           # building
    pyautogui.press('tab')
    pyautogui.typewrite('4')            # корпус
    pyautogui.press('tab')
    pyautogui.typewrite('6')            # house

################################## LIVING PLACE #####################

    pyautogui.press('tab')
    pyautogui.press('space')            # аналочно месту регистрации
    pyautogui._autoPause(1, 1)

################################## CONTACT #####################

    pyautogui.press('tab')
    for i in range(5):
        pyautogui.typewrite(personalData['mobile'])       # mobile phone
        pyautogui.press('tab')

    copyPaste(personalData['email'])    # type street


def create_personalData():    # function of generate new client data
    passport = ''
    person = Person('ru')

    # Выводим исландские мужские имена.

    lastname = person.last_name()
    personalData['lastname'] = lastname
    # print('\nфамилия:\t', personalData['lastname'])

    name = person.name()
    personalData['name'] = name
    # print('имя:\t\t', personalData['name'])

    surname = person.surname()
    personalData['surname'] = surname
    # print('отчество:\t', personalData['surname'])

    gender = person.gender()
    personalData['gender'] = gender
    # print('пол:\t\t', personalData['gender'])

    for _ in range(2):
        varLet = random.choice(string.ascii_uppercase)
        passport += varLet
    passport += person.telephone('#######')
    personalData['passport'] = passport
    # print('паспорт:\t', personalData['passport'])

### birthday
    currentDate()
    personalData['age'] = age
    personalData['age'][2] = str(int(personalData['age'][2]) - person.age(16, 70))
    # print('возраст:\t', personalData['age'], '\n')
###

    # print('гражд-во:\t', person.get_current_locale())
    # print('Нац-сть:\t',person.nationality())

### mobile
    mobile = person.telephone('+37529#######')
    personalData['mobile'] = mobile
    # print('телефон:\t', personalData['mobile'])
###
### email
    # personalData['email'] = person.email()
    # print('email:\t\t', personalData['email'])
###
    # print('проф-ия:\t', person.occupation(), '\n')
    # print('обращение:\t', person.title())
    # print('взгляды:\t', person.views_on())
    # print('вера:\t\t', person.worldview(), '\n')
    return personalData


create_personalData()
selfData(personalData)
# keys = str(input('Press "Space" and next "Enter" to repeat\nor "Enter" to exit\n').split())
# try:
#     while keys[0] == ' ':
#         create_personalData()
#         keys = input('Press "Space" and next "Enter" to create new client again\nor "Enter" to exit\n')
# except:
#     pass
