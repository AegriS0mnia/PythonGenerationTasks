class Pet:
    pets = []

    def __init__(self, name: str):
        self.__name = name
        Pet.pets.append(self)

    @property
    def name(self):
        return self.__name

    @classmethod
    def first_pet(cls):
        if Pet.pets:
            return Pet.pets[0]
        return None

    @classmethod
    def last_pet(cls):
        if Pet.pets:
            return Pet.pets[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        return len(Pet.pets)
