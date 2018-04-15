class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

dud = Person('Timmy', 25)
dud.first_name = 'Sebastian'
print(dud.show_age())


