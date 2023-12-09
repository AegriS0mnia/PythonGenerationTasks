class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def set_name(self, new_fullname):
        self.name, self.surname = new_fullname.split()

    fullname = property(get_fullname, set_name)


guy1 = Person('Henry', 'Dickenz')

print(guy1.__dict__)