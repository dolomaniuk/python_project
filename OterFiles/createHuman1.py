from mimesis import Person
import string
import random
import pyautogui
import xerox    # for ctrl+c/ctrl+v
from transliterate import translit, get_available_language_codes
from datetime import date

# pyautogui.PAUSE = 0.25
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



# def selfData(name, lname, surname, gend, latname, latlname)
def selfData(dict):
    xerox.copy(dict['lastname'])
    pyautogui.doubleClick(341, 246) # set cursor on Familiya
    pyautogui.hotkey('ctrl', 'v')

    xerox.copy(dict['name'])
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')     # type Name

    xerox.copy(dict['surname'])
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')     # type surname


    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('pageup')      # set default value
    pyautogui.press('pageup')

    if personalData['gender'] == 'Муж.':
        pyautogui.press('pagedown')    # set male
    else:
        pyautogui.press('pagedown')    # set female
        pyautogui.press('pagedown')

    xerox.copy(translit(dict['name'], 'ru', reversed=True))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')     # type latin Name
    xerox.copy(translit(dict['lastname'], 'ru', reversed=True))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')     # type latin LastName
    

def create_personalData():    # function of creating new client
    passport = ''
    person = Person('ru')

    # Выводим исландские мужские имена.
    
    lastname = person.last_name()
    personalData['lastname'] = lastname
    print('\nфамилия:\t', personalData['lastname'])

    name = person.name()
    personalData['name'] = name
    print('имя:\t\t', personalData['name'])

    surname = person.surname()
    personalData['surname'] = surname
    print('отчество:\t', personalData['surname'])

    gender = person.gender()
    personalData['gender'] = gender
    print('пол:\t\t', personalData['gender'])

    for _ in range(2):
        varLet = random.choice(string.ascii_uppercase)
        passport += varLet
    passport += person.telephone('#######')
    personalData['passport'] = passport
    print('паспорт:\t', personalData['passport'])

### birthday
    currentDate()
    personalData['age'] = age
    personalData['age'][2] = str(int(personalData['age'][2]) - person.age(16, 70))
    print('возраст:\t', personalData['age'], '\n')
###

    print('гражд-во:\t', person.get_current_locale())
    print('Нац-сть:\t',person.nationality())

### mobile
    mobile = person.telephone('+37529#######')
    personalData['mobile'] = mobile
    print('телефон:\t', personalData['mobile'])
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
